import pytest

from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from grpc_market.grpc.grpc_market_pb2_grpc import (
    RecetteControllerStub, add_RecetteControllerServicer_to_server)
from grpc_market.services.recette_service import RecetteService

from market.database.ingredient import Ingredient
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.metier import Metier
from market.database.recette import Recette

ingredient = Ingredient(name="Potion d'oubli", price=1000)
ingredient2 = Ingredient(name="Potion de soin", price=100)
ingredient3 = Ingredient(name="Potion de soin majeur", price=100)
ressource1 = Ingredient(name="Fleur de lin", price=5)
craft_ressource1 = IngredientForCraft(ingredient=ressource1, quantity=5)
ressource2 = Ingredient(name="Eau", price=1)
craft_ressource2 = IngredientForCraft(ingredient=ressource2, quantity=10)
metier = Metier(name="Cordonnier")
recette1 = Recette(ingredient=ingredient, level=100, metier=metier)
recette2 = Recette(ingredient=ingredient2, level=10, metier=metier)
recettes = [recette1, recette2]
craft_ingredients = [1, 2]  # PK of the IngredientForCraft object


@pytest.fixture
async def populate_database_with_test_data(request):
    await ingredient.asave()
    await ingredient2.asave()
    await ingredient3.asave()
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

    async def _cleanup_test_data():
        await ingredient.adelete()
        await ingredient2.adelete()
        await ressource1.adelete()
        await ressource2.adelete()
        await craft_ressource1.adelete()
        await craft_ressource2.adelete()
        await metier.adelete()
        await recette1.adelete()
        await recette2.adelete()

    request.addfinalizer(_cleanup_test_data)
