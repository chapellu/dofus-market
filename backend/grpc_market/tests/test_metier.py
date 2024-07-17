import json

import grpc
import pytest
from conftest import metier, metiers
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict

import grpc_market.grpc.grpc_market_pb2 as pb2
from grpc_market.grpc.grpc_market_p2p import (
    MetierDestroyRequest,
    MetierListRequest,
    MetierListResponse,
    MetierRequest,
    MetierResponse,
    MetierRetrieveRequest,
)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    MetierControllerStub,
    add_MetierControllerServicer_to_server,
)
from grpc_market.services.metier_service import MetierService
from market.database.metier import Metier


@pytest.fixture(autouse=True)
def grpc_client():
    fake_grpc = FakeFullAIOGRPC(
        add_MetierControllerServicer_to_server,
        MetierService.as_servicer(),
    )
    yield fake_grpc.get_fake_stub(MetierControllerStub)

    fake_grpc.close()


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__metier_to_string(populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    string = str(metier)

    # Then
    assert string == "Cordonnier"


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_metier__empty_list__ok(grpc_client):
    # Given

    # When
    request = MetierListRequest()
    response: pb2.MetierListResponse = await grpc_client.List(request)

    # Then
    assert response.results == []


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_metier__list_with_2_items__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data

    # When
    request = MetierListRequest()
    grpc_response: pb2.MetierListResponse = await grpc_client.List(request)
    response: MetierListResponse = MetierListResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert len(response.results) == len(metiers)
    for i in range(len(metiers)):
        assert response.results[i].name == metiers[i].name


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_metier__not_found(grpc_client):
    # Given

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = MetierRetrieveRequest(name=metier.name)
        await grpc_client.Retrieve(request)

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.NOT_FOUND
    assert json.loads(details) == {
        "message": f"Metier: {metier.name} not found!",
        "code": "not_found",
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_metier__ok(grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    expected_values = {"name": metier.name}

    # When
    request = MetierRetrieveRequest(name=metier.name)
    grpc_response: pb2.MetierResponse = await grpc_client.Retrieve(request)
    response: MetierResponse = MetierResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.model_dump() == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__create_metier__ok(grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data
    metier_name = "Tailleur"

    expected_values = {
        "name": metier_name,
    }

    # When
    request = MetierRequest(name=metier_name)
    grpc_response: pb2.MetierResponse = await grpc_client.Create(
        pb2.MetierRequest(**request.model_dump())
    )
    response: MetierResponse = MetierResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.model_dump() == expected_values

    metier: Metier = await Metier.objects.aget(name=metier_name)
    actual_values = {
        "name": metier.name,
    }
    assert actual_values == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__create_metier__already_exist(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = MetierRequest(name=metier.name)
        response: MetierResponse = await grpc_client.Create(
            pb2.MetierRequest(**request.model_dump())
        )

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.INVALID_ARGUMENT
    assert json.loads(details) == {
        "name": [{"message": "metier with this name already exists.", "code": "unique"}]
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__destroy_metier__ok(grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    request = MetierDestroyRequest(name=metier.name)
    response: Empty = await grpc_client.Destroy(request)

    # Then
    assert isinstance(response, Empty)
    with pytest.raises(Metier.DoesNotExist):
        await Metier.objects.aget(name=metier.name)


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__destroy_metier__does_not_exist(grpc_client):
    # Given
    metier_name = metier.name

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = MetierDestroyRequest(name=metier_name)
        response: Empty = await grpc_client.Destroy(request)

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.NOT_FOUND
    assert json.loads(details) == {
        "message": f"Metier: {metier_name} not found!",
        "code": "not_found",
    }
