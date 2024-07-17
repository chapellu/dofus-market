import json

import grpc
from grpc_market.serializers.equipement_serializer import (
    EquipementDetailsProtoSerializer,
)
from market.database.caracteristique import Caracteristique
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from conftest import (
    craft_ressource1,
    craft_ressource2,
    ingredient,
    ingredient2,
    equipement1,
)
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict
from grpc_market.grpc.grpc_market_p2p import (
    EquipementListRequest,
    EquipementListResponse,
    EquipementResponse,
    EquipementRetrieveRequest,
    EquipementDetailsRequest,
    EquipementDetailsResponse,
)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    EquipementControllerStub,
    add_EquipementControllerServicer_to_server,
)
from grpc_market.services.equipement_service import EquipementService
from market.database.materialized_views.orderered_by_rentability import (
    OrderedByRentability as Equipement,
)
from django.db import connection, connections
from asgiref.sync import sync_to_async, async_to_sync


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
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    await sync_to_async(refresh_materialized_view)()

    expected_values = {
        "name": equipement1.name,
        "level": equipement1.level,
        "cout_fabrication": 36.05,
        "gain_estime": 1350.0,
        "rentabilite": 3644,
        "nb_objet": 2,
        "metier": equipement1.metier.name,
    }

    # When
    request = EquipementListRequest()
    grpc_response: pb2.IngredientForCraftListResponse = await grpc_client.List(request)
    response: EquipementListResponse = EquipementListResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert len(response.results) == 1
    equipement = response.results[0]
    assert equipement.model_dump() == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_equipement__ok(grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data
    await sync_to_async(refresh_materialized_view)()

    expected_values = {
        "name": equipement1.name,
        "level": equipement1.level,
        "cout_fabrication": 36.05,
        "gain_estime": 1350.0,
        "rentabilite": 3644,
        "nb_objet": 2,
        "metier": equipement1.metier.name,
    }

    # When
    request = EquipementRetrieveRequest(name=equipement1.name)
    grpc_response: pb2.EquipementRetrieveRequest = await grpc_client.Retrieve(request)
    response: EquipementResponse = EquipementResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.model_dump() == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_equipement_details__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    await sync_to_async(refresh_materialized_view)()

    expected_values = {
        "name": "Marteau du Testeur",
        "level": 200,
        "cout_fabrication": 36.05,
        "gain_estime": 1350.0,
        "rentabilite": 3644.0,
        "nb_objet": 2,
        "metier": "Cordonnier",
        "effects": [
            {
                "name": "Agilité",
                "min": 50,
                "max": 100,
                "rune": {"name": "Age", "prix_ra": 1000, "prix_pa": 100, "prix_ba": 10},
            }
        ],
        "ingredients": [
            {
                "name": "Fleur de lin",
                "quantity": 5,
                "price": 5,
                "ingredients": [],
                "nb_objet": 0,
                "cout_fabrication": 0.0,
                "rentabilite": 0.0,
            },
            {
                "name": "Eau",
                "quantity": 10,
                "price": 1,
                "ingredients": [],
                "nb_objet": 0,
                "cout_fabrication": 0.0,
                "rentabilite": 0.0,
            },
        ],
        "brisage": [
            {
                "rune": "Age",
                "quantity_ra": 1.0,
                "prix_ra": 1000,
                "quantity_pa": 3.0,
                "prix_pa": 100,
                "quantity_ba": 5.0,
                "prix_ba": 10,
            }
        ],
    }

    # When
    request = EquipementDetailsRequest(name=equipement1.name)
    grpc_response: pb2.EquipementDetailsResponse = await grpc_client.Details(
        pb2.EquipementDetailsRequest(**request.model_dump())
    )
    response: EquipementDetailsResponse = EquipementDetailsResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.model_dump() == expected_values