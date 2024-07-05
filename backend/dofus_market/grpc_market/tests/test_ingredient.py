from django.test import TestCase, override_settings
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC

from market.database.ingredient import Ingredient
from grpc_market.grpc.grpc_market_pb2_grpc import add_IngredientControllerServicer_to_server, IngredientController, IngredientControllerStub, IngredientControllerServicer
from grpc_market.grpc.grpc_market_pb2 import IngredientListRequest, IngredientListResponse

from grpc_market.services.ingredient_service import IngredientService


@override_settings(GRPC_FRAMEWORK={"GRPC_ASYNC": True})
class TestPost(TestCase):
    def setUp(self):
        self.fake_grpc = FakeFullAIOGRPC(
            add_IngredientControllerServicer_to_server,
            IngredientService.as_servicer(),
        )

    def tearDown(self) -> None:
        self.fake_grpc.close()


    async def test__list_ingredient__empty_list__ok(self):
        # Given
        client = self.fake_grpc.get_fake_stub(IngredientControllerStub)

        # When
        request = IngredientListRequest()
        response: IngredientListResponse = await client.List(request)

        # Then
        self.assertEqual(response.results, [])

    async def test__list_ingredient__list_with_2_items__ok(self):
        # Given
        ingredients = []
        ingredients.append(await Ingredient.objects.acreate(
            name="Laine de Bouftou",
            price=10
        ))
        ingredients.append(await Ingredient.objects.acreate(
            name="Bave de Bouftou",
            price=100
        ))
        client = self.fake_grpc.get_fake_stub(IngredientControllerStub)

        # When
        request = IngredientListRequest()
        response: IngredientListResponse = await client.List(request)

        # Then
        self.assertEqual(len(response.results), len(ingredients))
        for i in range(len(ingredients)):
            self.assertEqual(response.results[i].name, ingredients[i].name)
            self.assertEqual(response.results[i].price, ingredients[i].price)
