import json

import grpc
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from conftest import craft_ressource1, craft_ressource2, ingredient, ingredient2
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict
from grpc_market.grpc.grpc_market_p2p import (
    IngredientForCraftDestroyRequest,
    IngredientForCraftListRequest,
    IngredientForCraftListResponse,
    IngredientForCraftRequest,
    IngredientForCraftResponse,
    IngredientForCraftRetrieveRequest,
)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    IngredientForCraftControllerStub,
    add_IngredientForCraftControllerServicer_to_server,
)
from grpc_market.services.ingredient_for_craft_service import IngredientForCraftService
from market.database.ingredient_for_craft import IngredientForCraft


@pytest.fixture(autouse=True)
def grpc_client():
    fake_grpc = FakeFullAIOGRPC(
        add_IngredientForCraftControllerServicer_to_server,
        IngredientForCraftService.as_servicer(),
    )
    yield fake_grpc.get_fake_stub(IngredientForCraftControllerStub)

    fake_grpc.close()


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__ingredient_for_craft_to_string(populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    string = str(craft_ressource1)

    # Then
    assert string == '{name: "Fleur de lin", quantity: 5}'


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_ingredient_for_craft__empty_list__ok(grpc_client):
    # Given

    # When
    request = IngredientForCraftListRequest()
    response: pb2.IngredientForCraftListResponse = await grpc_client.List(request)

    # Then
    assert response.results == []


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_ingredient_for_craft__list_with_2_items__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    ingredient_for_crafts = [craft_ressource1, craft_ressource2]

    # When
    request = IngredientForCraftListRequest()
    grpc_response: pb2.IngredientForCraftListResponse = await grpc_client.List(request)
    response: IngredientForCraftListResponse = IngredientForCraftListResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert len(response.results) == len(ingredient_for_crafts)
    for i in range(len(ingredient_for_crafts)):
        assert (
            response.results[i].ingredient == ingredient_for_crafts[i].ingredient.name
        )
        assert response.results[i].quantity == ingredient_for_crafts[i].quantity


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_ingredient_for_craft__not_found(grpc_client):
    # Given
    ingredient_for_craft_id = 0

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = IngredientForCraftRetrieveRequest(id=ingredient_for_craft_id)
        await grpc_client.Retrieve(request)

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.NOT_FOUND
    assert json.loads(details) == {
        "message": f"IngredientForCraft: {ingredient_for_craft_id} not found!",
        "code": "not_found",
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_ingredient_for_craft__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data

    expected_values = {
        "id": craft_ressource1.pk,
        "ingredient": craft_ressource1.ingredient.name,
        "quantity": craft_ressource1.quantity,
    }

    # When
    request = IngredientForCraftRetrieveRequest(id=craft_ressource1.pk)
    grpc_response: pb2.IngredientForCraftResponse = await grpc_client.Retrieve(request)
    response: IngredientForCraftResponse = IngredientForCraftResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.model_dump() == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__create_ingredient_for_craft__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    ingredient_name = ingredient.name
    quantity = 5
    expected_id = 3

    expected_values = {
        "id": expected_id,
        "ingredient": ingredient_name,
        "quantity": quantity,
    }

    # When
    request = IngredientForCraftRequest(ingredient=ingredient_name, quantity=quantity)
    grpc_response: pb2.IngredientForCraftResponse = await grpc_client.Create(
        pb2.IngredientForCraftRequest(**request.model_dump())
    )
    response: IngredientForCraftResponse = IngredientForCraftResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.model_dump() == expected_values

    ingredient_for_craft: IngredientForCraft = await IngredientForCraft.objects.aget(
        id=expected_id
    )
    actual_values = {
        "id": ingredient_for_craft.pk,
        "ingredient": ingredient_for_craft.ingredient_id,
        "quantity": ingredient_for_craft.quantity,
    }
    assert actual_values == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__create_ingredient_for_craft__already_exist(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    ingredient_name = craft_ressource1.ingredient.name
    quantity = craft_ressource1.quantity
    _id = craft_ressource1.pk

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = IngredientForCraftRequest(
            ingredient=ingredient_name, quantity=quantity
        )
        response: IngredientForCraftResponse = await grpc_client.Create(
            pb2.IngredientForCraftRequest(**request.model_dump())
        )

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.INVALID_ARGUMENT
    assert json.loads(details) == {
        "non_field_errors": [
            {
                "message": "The fields ingredient, quantity must make a unique set.",
                "code": "unique",
            }
        ]
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__destroy_ingredient_for_craft__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data

    # When
    request = IngredientForCraftDestroyRequest(id=craft_ressource1.pk)
    response: Empty = await grpc_client.Destroy(request)

    # Then
    assert isinstance(response, Empty)
    with pytest.raises(IngredientForCraft.DoesNotExist):
        await IngredientForCraft.objects.aget(id=craft_ressource1.pk)


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__destroy_ingredient_for_craft__does_not_exist(grpc_client):
    # Given
    ingredient_for_craft_id = 1

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = IngredientForCraftDestroyRequest(id=ingredient_for_craft_id)
        response: Empty = await grpc_client.Destroy(request)

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.NOT_FOUND
    assert json.loads(details) == {
        "message": f"IngredientForCraft: {ingredient_for_craft_id} not found!",
        "code": "not_found",
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__update_ingredient_for_craft__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    new_ingredient = ingredient2.name
    new_quantity = 1

    # When
    request = IngredientForCraftRequest(
        id=craft_ressource1.pk, ingredient=new_ingredient, quantity=new_quantity
    )
    grpc_response: pb2.IngredientForCraftResponse = await grpc_client.Update(
        pb2.IngredientForCraftRequest(**request.model_dump())
    )
    response: IngredientForCraftResponse = IngredientForCraftResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.ingredient == new_ingredient
    assert response.quantity == new_quantity
    ingredient_for_craft = await IngredientForCraft.objects.aget(id=craft_ressource1.pk)
    assert ingredient_for_craft.ingredient_id == new_ingredient
    assert ingredient_for_craft.quantity == new_quantity


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__partial_update_ingredient_for_craft__ok(
    grpc_client, populate_database_with_test_data
):
    # Given
    await populate_database_with_test_data
    new_quantity = 1

    # When
    request = pb2.IngredientForCraftPartialUpdateRequest(
        id=craft_ressource1.pk,
        quantity=new_quantity,
        _partial_update_fields=["quantity"],
    )
    grpc_response: pb2.IngredientForCraftResponse = await grpc_client.PartialUpdate(
        request
    )
    response: IngredientForCraftResponse = IngredientForCraftResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True)
    )

    # Then
    assert response.ingredient == craft_ressource1.ingredient.name
    assert response.quantity == new_quantity
    ingredient_for_craft = await IngredientForCraft.objects.aget(id=craft_ressource1.pk)
    assert ingredient_for_craft.ingredient_id == craft_ressource1.ingredient.name
    assert ingredient_for_craft.quantity == new_quantity
