from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from grpc_market.services.ingredient_service import IngredientService
from grpc_market.services.rune_service import RuneService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("grpc_market", server)
    app_registry.register(IngredientService)
    app_registry.register(RuneService)
