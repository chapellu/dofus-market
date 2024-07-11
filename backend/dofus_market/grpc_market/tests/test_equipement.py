import json

import grpc
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from conftest import craft_ressource1, craft_ressource2, ingredient, ingredient2, equipement1
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict
from grpc_market.grpc.grpc_market_p2p import (EquipementListRequest,
                                              EquipementListResponse,
                                              EquipementResponse,
                                              EquipementRetrieveRequest)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    EquipementControllerStub, add_EquipementControllerServicer_to_server)
from grpc_market.services.equipement_service import EquipementService
from market.database.materialized_views.orderered_by_rentability import OrderedByRentability as Equipement
from django.db import connection, connections
from asgiref.sync import sync_to_async


@pytest.fixture(autouse=True)
def grpc_client():
    fake_grpc = FakeFullAIOGRPC(
        add_EquipementControllerServicer_to_server,
        EquipementService.as_servicer(),
    )
    yield fake_grpc.get_fake_stub(EquipementControllerStub)

    fake_grpc.close()


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_equipement__empty_list__ok(grpc_client):
    # Given

    # When
    request = EquipementListRequest()
    response: pb2.EquipementListResponse = await grpc_client.List(request)

    # Then
    assert response.results == []


def refresh_materialized_view():
    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW FabricationCosts;")
        cursor.execute("REFRESH MATERIALIZED VIEW EstimatedGains;")
        cursor.execute("REFRESH MATERIALIZED VIEW Rentability;")
        cursor.execute("REFRESH MATERIALIZED VIEW OrderedByRentability;")


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_equipement__list_with_1_item__ok(
        grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data
    await sync_to_async(refresh_materialized_view)()

    expected_values = {
        "name": equipement1.name,
        "level": equipement1.level,
        "cout_fabrication": 25.75,
        "gain_estime": 1350.0,
        "rentabilite": 5142,
        "nb_object": 1,
        "metier": equipement1.metier.name,
    }

    # When
    request = EquipementListRequest()
    grpc_response: pb2.IngredientForCraftListResponse = await grpc_client.List(
        request)
    response: EquipementListResponse = EquipementListResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True))

    # Then
    assert len(response.results) == 1
    equipement = response.results[0]
    assert equipement.model_dump() == expected_values
