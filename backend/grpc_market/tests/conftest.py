import pytest
from asgiref.sync import async_to_sync

from market.database.caracteristique import Caracteristique
from market.database.equipement import DofusObject as Equipement
from market.database.ingredient import Ingredient
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.metier import Metier
from market.database.recette import Recette
from market.database.rune import Rune

ingredient = Ingredient(name="Potion d'oubli", price=1000)
ingredient2 = Ingredient(name="Potion de soin", price=100)
ingredient3 = Ingredient(name="Potion de soin majeur", price=100)
ressource1 = Ingredient(name="Fleur de lin", price=5)
craft_ressource1 = IngredientForCraft(ingredient=ressource1, quantity=5)
ressource2 = Ingredient(name="Eau", price=1)
craft_ressource2 = IngredientForCraft(ingredient=ressource2, quantity=10)
metier = Metier(name="Cordonnier")
metier2 = Metier(name="Alchimiste")
recette1 = Recette(ingredient=ingredient, level=100, metier=metier)
recette2 = Recette(ingredient=ingredient2, level=10, metier=metier)
recettes = [recette1, recette2]
craft_ingredients = [1, 2]  # PK of the IngredientForCraft object
metiers = [metier, metier2]

equipement1 = Equipement(name="Marteau du Testeur", level=200, metier=metier)
rune1 = Rune(name="Age", prix_ra=1000, prix_pa=100, prix_ba=10)
caracteristique1 = Caracteristique(
    name="Agilité",
    min=50,
    max=100,
    rune=rune1,
    level=equipement1.level,
    number_of_ra=1,
    number_of_pa=3,
    number_of_ba=5,
)


@pytest.fixture(autouse=True)
def enable_transactional_db_access_for_all_tests(transactional_db):
    pass


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
    await metier2.asave()
    await recette1.asave()
    await recette2.asave()
    await rune1.asave()
    await caracteristique1.asave()
    await equipement1.asave()

    await recette1.ingredients.aadd(craft_ressource1)
    await recette1.ingredients.aadd(craft_ressource2)
    await recette2.ingredients.aadd(craft_ressource1)
    await recette2.ingredients.aadd(craft_ressource2)

    await equipement1._effects.aadd(caracteristique1)
    await equipement1._ingredients.aadd(craft_ressource1)
    await equipement1._ingredients.aadd(craft_ressource2)

    async def _cleanup_test_data():
        await ingredient.adelete()
        await ingredient2.adelete()
        await ingredient3.adelete()
        await ressource1.adelete()
        await ressource2.adelete()
        await craft_ressource1.adelete()
        await craft_ressource2.adelete()
        await metier.adelete()
        await metier2.adelete()
        await recette1.adelete()
        await recette2.adelete()
        await rune1.adelete()
        await caracteristique1.adelete()
        await equipement1.adelete()

    request.addfinalizer(lambda: async_to_sync(_cleanup_test_data))
