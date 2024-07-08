import grpc
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from django.test import TestCase, override_settings
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from grpc_market.grpc.grpc_market_p2p import (
    IngredientDestroyRequest, IngredientListRequest, IngredientListResponse,
    IngredientRequest, IngredientResponse, IngredientRetrieveRequest)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    IngredientControllerStub, add_IngredientControllerServicer_to_server)
from grpc_market.services.ingredient_service import IngredientService
from market.database.ingredient import Ingredient


@override_settings(GRPC_FRAMEWORK={"GRPC_ASYNC": True})
class TestPost(TestCase):

    def setUp(self):
        self.fake_grpc = FakeFullAIOGRPC(
            add_IngredientControllerServicer_to_server,
            IngredientService.as_servicer(),
        )
        self.client: IngredientControllerStub = self.fake_grpc.get_fake_stub(
            IngredientControllerStub)

    def tearDown(self) -> None:
        self.fake_grpc.close()

    async def test__ingredient_to_string(self):
        # Given
        ingredient = Ingredient(name="Laine de Bouftou", price=10)

        # When
        string = str(ingredient)

        # Then
        self.assertEqual(string, "Laine de Bouftou")

    async def test__list_ingredient__empty_list__ok(self):
        # Given

        # When
        request = IngredientListRequest()
        response: IngredientListResponse = await self.client.List(request)

        # Then
        self.assertEqual(response.results, [])

    async def test__list_ingredient__list_with_2_items__ok(self):
        # Given
        ingredients = []
        ingredients.append(await
                           Ingredient.objects.acreate(name="Laine de Bouftou",
                                                      price=10))
        ingredients.append(await
                           Ingredient.objects.acreate(name="Bave de Bouftou",
                                                      price=100))

        # When
        request = IngredientListRequest()
        response: IngredientListResponse = await self.client.List(request)

        # Then
        self.assertEqual(len(response.results), len(ingredients))
        for i in range(len(ingredients)):
            self.assertEqual(response.results[i].name, ingredients[i].name)
            self.assertEqual(response.results[i].price, ingredients[i].price)

    async def test__retrieve_ingredient__not_found(self):
        # Given
        ingredient_name = "Laine de Bouftou"

        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = IngredientRetrieveRequest(name=ingredient_name)
            await self.client.Retrieve(request)

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.NOT_FOUND)
        self.assertEqual(
            expected_error.value.args[1],
            f'{{"message": "Ingredient: {ingredient_name} not found!", "code": "not_found"}}'
        )

    async def test__retrieve_ingredient__ok(self):
        # Given
        ingredient_name = "Laine de Bouftou"
        ingredient_price = 10
        await Ingredient.objects.acreate(name=ingredient_name,
                                         price=ingredient_price)
        # When
        request = IngredientRetrieveRequest(name=ingredient_name)
        response: IngredientResponse = await self.client.Retrieve(request)

        # Then
        self.assertEqual(response.name, ingredient_name)
        self.assertEqual(response.price, ingredient_price)

    async def test__create_ingredient__ok(self):
        # Given
        ingredient_name = "Laine de Bouftou"
        ingredient_price = 10

        # When
        request = IngredientRequest(name=ingredient_name,
                                    price=ingredient_price)
        response: IngredientResponse = await self.client.Create(
            pb2.IngredientRequest(**request.model_dump()))

        # Then
        self.assertEqual(response.name, ingredient_name)
        self.assertEqual(response.price, ingredient_price)
        ingredient = await Ingredient.objects.aget(name=ingredient_name)
        self.assertEqual(ingredient.name, ingredient_name)
        self.assertEqual(ingredient.price, ingredient_price)

    async def test__create_ingredient__already_exist(self):
        # Given
        ingredient_name = "Laine de Bouftou"
        ingredient_price = 10
        await Ingredient.objects.acreate(name=ingredient_name,
                                         price=ingredient_price)
        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = IngredientRequest(name=ingredient_name,
                                        price=ingredient_price)
            response: IngredientResponse = await self.client.Create(
                pb2.IngredientRequest(**request.model_dump()))

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.INVALID_ARGUMENT)
        self.assertEqual(
            expected_error.value.args[1],
            '{"name": [{"message": "ingredient with this name already exists.", "code": "unique"}]}'
        )

    async def test__destroy_ingredient__ok(self):
        # Given
        ingredient_name = "Laine de Bouftou"
        ingredient_price = 10
        await Ingredient.objects.acreate(name=ingredient_name,
                                         price=ingredient_price)

        # When
        request = IngredientDestroyRequest(name=ingredient_name)
        response: Empty = await self.client.Destroy(request)

        # Then
        self.assertTrue(isinstance(response, Empty))
        with pytest.raises(Ingredient.DoesNotExist):
            await Ingredient.objects.aget(name=ingredient_name)

    async def test__destroy_ingredient__does_not_exist(self):
        # Given
        ingredient_name = "Laine de Bouftou"
        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = IngredientDestroyRequest(name=ingredient_name)
            response: Empty = await self.client.Destroy(request)

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.NOT_FOUND)
        self.assertEqual(
            expected_error.value.args[1],
            f'{{"message": "Ingredient: {ingredient_name} not found!", "code": "not_found"}}'
        )

    async def test__update_ingredient__ok(self):
        # Given
        ingredient_name = "Laine de Bouftou"
        old_ingredient_price = 10
        new_ingredient_price = 100
        await Ingredient.objects.acreate(name=ingredient_name,
                                         price=old_ingredient_price)

        # When
        request = IngredientRequest(name=ingredient_name,
                                    price=new_ingredient_price)
        response: IngredientResponse = await self.client.Update(
            pb2.IngredientRequest(**request.model_dump()))

        # Then
        self.assertEqual(response.name, ingredient_name)
        self.assertEqual(response.price, new_ingredient_price)
        ingredient = await Ingredient.objects.aget(name=ingredient_name)
        self.assertEqual(ingredient.name, ingredient_name)
        self.assertEqual(ingredient.price, new_ingredient_price)
