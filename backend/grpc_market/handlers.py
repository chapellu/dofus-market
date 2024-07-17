from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from grpc_market.services.recette_service import RecetteService
from grpc_market.services.ingredient_service import IngredientService
from grpc_market.services.rune_service import RuneService
from grpc_market.services.metier_service import MetierService
from grpc_market.services.ingredient_for_craft_service import IngredientForCraftService
from grpc_market.services.equipement_service import EquipementService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("grpc_market", server)
    app_registry.register(IngredientService)
    app_registry.register(RuneService)
    app_registry.register(RecetteService)
    app_registry.register(MetierService)
    app_registry.register(IngredientForCraftService)
    app_registry.register(EquipementService)
