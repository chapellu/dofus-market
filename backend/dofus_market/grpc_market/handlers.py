from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry

from grpc_market.services.ingredient_service import IngredientService

def grpc_handlers(server):
    app_registry = AppHandlerRegistry("grpc_market", server)
    app_registry.register(IngredientService)