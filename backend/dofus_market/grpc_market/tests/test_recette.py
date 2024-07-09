import grpc
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.metier import Metier
from market.database.ingredient import Ingredient
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from django.test import TestCase, override_settings
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from grpc_market.grpc.grpc_market_p2p import (RecetteDestroyRequest,
                                              RecetteListRequest,
                                              RecetteListResponse,
                                              RecetteRequest, RecetteResponse,
                                              RecetteRetrieveRequest)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    RecetteControllerStub, add_RecetteControllerServicer_to_server)
from grpc_market.services.recette_service import RecetteService
from market.database.recette import Recette
from asgiref.sync import sync_to_async

ingredient = Ingredient(name="Potion d'oubli", price=1000)
ingredient2 = Ingredient(name="Potion de soin", price=100)
ressource1 = Ingredient(name="Fleur de lin", price=5)
craft_ressource1 = IngredientForCraft(ingredient=ressource1, quantity=5)
ressource2 = Ingredient(name="Eau", price=1)
craft_ressource2 = IngredientForCraft(ingredient=ressource2, quantity=10)
metier = Metier(name="Cordonnier")
recette1 = Recette(ingredient=ingredient, level=100, metier=metier)
recette2 = Recette(ingredient=ingredient2, level=10, metier=metier)


@override_settings(GRPC_FRAMEWORK={"GRPC_ASYNC": True})
class TestRecette(TestCase):

    def setUp(self):
        self.fake_grpc = FakeFullAIOGRPC(
            add_RecetteControllerServicer_to_server,
            RecetteService.as_servicer(),
        )
        self.client: RecetteControllerStub = self.fake_grpc.get_fake_stub(
            RecetteControllerStub)

    def tearDown(self) -> None:
        self.fake_grpc.close()

    async def test__recette_to_string(self):
        # Given
        recette = recette1

        # When
        string = str(recette)

        # Then
        self.assertEqual(string, "Potion d'oubli")

    async def test__list_recette__empty_list__ok(self):
        # Given

        # When
        request = RecetteListRequest()
        response: RecetteListResponse = await self.client.List(request)

        # Then
        self.assertEqual(response.results, [])

    async def test__list_recette__list_with_2_items__ok(self):
        # Given
        await ingredient.asave()
        await ingredient2.asave()
        await ressource1.asave()
        await ressource2.asave()
        await craft_ressource1.asave()
        await craft_ressource2.asave()
        await metier.asave()
        await recette1.asave()
        await recette2.asave()
        await recette1.ingredients.aadd(craft_ressource1)
        await recette1.ingredients.aadd(craft_ressource2)
        await recette2.ingredients.aadd(craft_ressource1)
        await recette2.ingredients.aadd(craft_ressource2)
        recettes = [recette1, recette2]
        craft_ingredients = [craft_ressource1.pk, craft_ressource2.pk]

        # When
        request = RecetteListRequest()
        response: RecetteListResponse = await self.client.List(request)

        # Then
        self.assertEqual(len(response.results), len(recettes))
        for i in range(len(recettes)):
            self.assertEqual(response.results[i].ingredient,
                             recettes[i].ingredient.name)
            self.assertEqual(response.results[i].level, recettes[i].level)
            self.assertEqual(response.results[i].metier,
                             recettes[i].metier.name)
            self.assertEqual(response.results[i].ingredients,
                             craft_ingredients)

    async def test__retrieve_recette__not_found(self):
        # Given

        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = RecetteRetrieveRequest(ingredient=ingredient.name)
            await self.client.Retrieve(request)

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.NOT_FOUND)
        self.assertEqual(
            expected_error.value.args[1],
            f'{{"message": "Recette: {ingredient.name} not found!", "code": "not_found"}}'
        )

    async def test__retrieve_recette__ok(self):
        # Given
        await ingredient.asave()
        await metier.asave()
        await recette1.asave()
        await ressource1.asave()
        await ressource2.asave()
        await craft_ressource1.asave()
        await craft_ressource2.asave()
        await recette1.ingredients.aadd(craft_ressource1)
        await recette1.ingredients.aadd(craft_ressource2)
        craft_ingredients = [craft_ressource1.pk, craft_ressource2.pk]

        # When
        request = RecetteRetrieveRequest(ingredient=recette1.ingredient.name)
        response: RecetteResponse = await self.client.Retrieve(request)

        # Then
        self.assertEqual(response.ingredient, recette1.ingredient.name)
        self.assertEqual(response.level, recette1.level)
        self.assertEqual(response.metier, recette1.metier.name)
        self.assertEqual(response.ingredients, craft_ingredients)

    async def test__create_recette__ok(self):
        # Given
        await ingredient.asave()
        await metier.asave()
        await ressource1.asave()
        await ressource2.asave()
        await craft_ressource1.asave()
        await craft_ressource2.asave()

        # When
        request = RecetteRequest(
            ingredient=recette1.ingredient.name,
            level=recette1.level,
            metier=recette1.metier.name,
            ingredients=[craft_ressource1.pk, craft_ressource2.pk])
        response: RecetteResponse = await self.client.Create(
            pb2.RecetteRequest(**request.model_dump()))

        # Then
        self.assertEqual(response.ingredient, recette1.ingredient.name)
        self.assertEqual(response.level, recette1.level)
        self.assertEqual(response.metier, recette1.metier.name)
        self.assertEqual(len(response.ingredients), 2)
        self.assertEqual(response.ingredients[0], craft_ressource1.pk)
        self.assertEqual(response.ingredients[1], craft_ressource2.pk)
        recette = await Recette.objects.aget(
            ingredient=recette1.ingredient.name)
        self.assertEqual(recette.ingredient_id, recette1.ingredient.name)
        self.assertEqual(recette.level, recette1.level)
        self.assertEqual(recette.metier_id, recette1.metier.name)
        ingredients = await sync_to_async(list)(recette.ingredients.all())
        self.assertEqual(len(ingredients), 2)
        self.assertEqual(ingredients[0].pk, craft_ressource1.pk)
        self.assertEqual(ingredients[1].pk, craft_ressource2.pk)

    async def test__create_recette__already_exist(self):
        # Given
        await ingredient.asave()
        await metier.asave()
        await recette1.asave()
        await ressource1.asave()
        await ressource2.asave()
        await craft_ressource1.asave()
        await craft_ressource2.asave()
        await recette1.ingredients.aadd(craft_ressource1)
        await recette1.ingredients.aadd(craft_ressource2)

        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = RecetteRequest(
                ingredient=recette1.ingredient.name,
                level=recette1.level,
                metier=recette1.metier.name,
                ingredients=[craft_ressource1.pk, craft_ressource2.pk])
            response: RecetteResponse = await self.client.Create(
                pb2.RecetteRequest(**request.model_dump()))

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.INVALID_ARGUMENT)
        self.assertEqual(
            expected_error.value.args[1],
            '{"ingredient": [{"message": "recette with this ingredient already exists.", "code": "unique"}]}'
        )

    async def test__destroy_recette__ok(self):
        # Given
        await ingredient.asave()
        await metier.asave()
        await recette1.asave()
        await ressource1.asave()
        await ressource2.asave()
        await craft_ressource1.asave()
        await craft_ressource2.asave()
        await recette1.ingredients.aadd(craft_ressource1)
        await recette1.ingredients.aadd(craft_ressource2)

        # When
        request = RecetteDestroyRequest(ingredient=recette1.ingredient.name)
        response: Empty = await self.client.Destroy(request)

        # Then
        self.assertTrue(isinstance(response, Empty))
        with pytest.raises(Recette.DoesNotExist):
            await Recette.objects.aget(ingredient=recette1.ingredient.name)

    async def test__destroy_recette__does_not_exist(self):
        # Given
        recette_name = ingredient.name

        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = RecetteDestroyRequest(ingredient=recette_name)
            response: Empty = await self.client.Destroy(request)

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.NOT_FOUND)
        self.assertEqual(
            expected_error.value.args[1],
            f'{{"message": "Recette: {recette_name} not found!", "code": "not_found"}}'
        )

    async def test__update_recette__ok(self):
        # Given
        await ingredient.asave()
        await metier.asave()
        await recette1.asave()
        await ressource1.asave()
        await ressource2.asave()
        await craft_ressource1.asave()
        await craft_ressource2.asave()
        await recette1.ingredients.aadd(craft_ressource1)
        await recette1.ingredients.aadd(craft_ressource2)

        new_metier = await Metier.objects.acreate(name="Tailleur")

        # When
        request = RecetteRequest(ingredient=recette1.ingredient.name,
                                 level=recette1.level + 10,
                                 metier=new_metier.name,
                                 ingredients=[craft_ressource1.pk])
        response: RecetteResponse = await self.client.Update(
            pb2.RecetteRequest(**request.model_dump()))

        # Then
        self.assertEqual(response.ingredient, recette1.ingredient.name)
        self.assertEqual(response.level, recette1.level + 10)
        self.assertEqual(response.metier, new_metier.name)
        self.assertEqual(len(response.ingredients), 1)
        self.assertEqual(response.ingredients[0], craft_ressource1.pk)
        recette = await Recette.objects.aget(
            ingredient=recette1.ingredient.name)
        self.assertEqual(recette.ingredient_id, recette1.ingredient.name)
        self.assertEqual(recette.level, recette1.level + 10)
        self.assertEqual(recette.metier_id, new_metier.name)
        ingredients = await sync_to_async(list)(recette.ingredients.all())
        self.assertEqual(len(ingredients), 1)
        self.assertEqual(ingredients[0].pk, craft_ressource1.pk)
