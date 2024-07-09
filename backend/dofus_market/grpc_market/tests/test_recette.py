import json
import grpc
from market.database.ingredient_for_craft import IngredientForCraft
from market.database.metier import Metier
from market.database.ingredient import Ingredient
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from django.test import TestCase, override_settings
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from grpc_market.grpc.grpc_market_p2p import (RecetteDestroyRequest,
                                              RecetteListRequest,
                                              RecetteListResponse,
                                              RecetteRequest, RecetteResponse,
                                              RecetteRetrieveRequest)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    RecetteControllerStub, add_RecetteControllerServicer_to_server)
from grpc_market.services.recette_service import RecetteService
from market.database.recette import Recette
from asgiref.sync import sync_to_async
from google.protobuf.json_format import MessageToDict
from django.forms.models import model_to_dict

from conftest import ingredient, ingredient2, ressource1, ressource2, craft_ressource1, craft_ressource2, metier, recette1, recette2, recettes, craft_ingredients


@pytest.fixture(autouse=True)
def grpc_client():
    fake_grpc = FakeFullAIOGRPC(
        add_RecetteControllerServicer_to_server,
        RecetteService.as_servicer(),
    )
    yield fake_grpc.get_fake_stub(RecetteControllerStub)

    fake_grpc.close()


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__recette_to_string(populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    string = str(recette1)

    # Then
    assert string == "Potion d'oubli"


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_recette__empty_list__ok(grpc_client):
    # Given

    # When
    request = RecetteListRequest()
    response: pb2.RecetteListResponse = await grpc_client.List(request)

    # Then
    assert response.results == []


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__list_recette__list_with_2_items__ok(
        grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    request = RecetteListRequest()
    grpc_response: pb2.RecetteListResponse = await grpc_client.List(request)
    response: RecetteListResponse = RecetteListResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True))

    # Then
    assert len(response.results) == len(recettes)
    for i in range(len(recettes)):
        assert response.results[i].ingredient == recettes[i].ingredient.name
        assert response.results[i].level == recettes[i].level
        assert response.results[i].metier == recettes[i].metier.name
        assert response.results[i].ingredients == craft_ingredients


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_recette__not_found(grpc_client):
    # Given

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = RecetteRetrieveRequest(ingredient=ingredient.name)
        await grpc_client.Retrieve(request)

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.NOT_FOUND
    assert json.loads(details) == {
        "message": f"Recette: {ingredient.name} not found!",
        "code": "not_found"
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__retrieve_recette__ok(grpc_client,
                                     populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    expected_values = {
        "ingredient": recette1.ingredient.name,
        "level": recette1.level,
        "metier": recette1.metier.name,
        "ingredients": craft_ingredients
    }

    # When
    request = RecetteRetrieveRequest(ingredient=recette1.ingredient.name)
    grpc_response: pb2.RecetteResponse = await grpc_client.Retrieve(request)
    response: RecetteResponse = RecetteResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True))

    # Then
    assert response.model_dump() == expected_values


async def async_model_to_dict(instance):
    sync_model_to_dict = sync_to_async(model_to_dict, thread_sensitive=True)
    return await sync_model_to_dict(instance)


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__create_recette__ok(grpc_client,
                                   populate_database_with_test_data):
    # Given
    await populate_database_with_test_data
    ingredient_name = "Potion de soin majeur"
    level = 53
    metier = "Cordonnier"
    ingredients = [craft_ressource1.pk, craft_ressource2.pk]

    expected_values = {
        "ingredient": ingredient_name,
        "level": level,
        "metier": metier,
        "ingredients": ingredients
    }

    # When
    request = RecetteRequest(ingredient=ingredient_name,
                             level=level,
                             metier=metier,
                             ingredients=ingredients)
    grpc_response: pb2.RecetteResponse = await grpc_client.Create(
        pb2.RecetteRequest(**request.model_dump()))
    response: RecetteResponse = RecetteResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True))

    # Then
    assert response.model_dump() == expected_values

    recette: Recette = await Recette.objects.aget(ingredient=ingredient_name)
    ingredients = await sync_to_async(list)(recette.ingredients.all())
    actual_values = {
        "ingredient": recette.ingredient_id,
        "level": recette.level,
        "metier": recette.metier_id,
        "ingredients": [ingredient.pk for ingredient in ingredients]
    }
    assert actual_values == expected_values


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__create_recette__already_exist(
        grpc_client, populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = RecetteRequest(
            ingredient=recette1.ingredient.name,
            level=recette1.level,
            metier=recette1.metier.name,
            ingredients=[craft_ressource1.pk, craft_ressource2.pk])
        response: RecetteResponse = await grpc_client.Create(
            pb2.RecetteRequest(**request.model_dump()))

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.INVALID_ARGUMENT
    assert json.loads(details) == {
        "ingredient": [{
            "message": "recette with this ingredient already exists.",
            "code": "unique"
        }]
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__destroy_recette__ok(grpc_client,
                                    populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    # When
    request = RecetteDestroyRequest(ingredient=recette1.ingredient.name)
    response: Empty = await grpc_client.Destroy(request)

    # Then
    assert isinstance(response, Empty)
    with pytest.raises(Recette.DoesNotExist):
        await Recette.objects.aget(ingredient=recette1.ingredient.name)


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__destroy_recette__does_not_exist(grpc_client):
    # Given
    recette_name = ingredient.name

    # When
    with pytest.raises(grpc.RpcError) as expected_error:
        request = RecetteDestroyRequest(ingredient=recette_name)
        response: Empty = await grpc_client.Destroy(request)

    # Then
    code, details = expected_error.value.args
    assert code == grpc.StatusCode.NOT_FOUND
    assert json.loads(details) == {
        "message": f"Recette: {recette_name} not found!",
        "code": "not_found"
    }


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test__update_recette__ok(grpc_client,
                                   populate_database_with_test_data):
    # Given
    await populate_database_with_test_data

    new_level = recette1.level + 10
    new_metier = await Metier.objects.acreate(name="Tailleur")
    new_ingredients = [craft_ressource1.pk]
    expected_values = {
        "ingredient": recette1.ingredient.name,
        "level": new_level,
        "metier": new_metier.name,
        "ingredients": new_ingredients
    }

    # When
    request = RecetteRequest(ingredient=recette1.ingredient.name,
                             level=new_level,
                             metier=new_metier.name,
                             ingredients=new_ingredients)
    grpc_response: pb2.RecetteResponse = await grpc_client.Update(
        pb2.RecetteRequest(**request.model_dump()))
    response: RecetteResponse = RecetteResponse(
        **MessageToDict(grpc_response, preserving_proto_field_name=True))

    # Then
    assert response.model_dump() == expected_values

    recette = await Recette.objects.aget(ingredient=recette1.ingredient.name)
    ingredients = await sync_to_async(list)(recette.ingredients.all())
    actual_values = {
        "ingredient": recette.ingredient_id,
        "level": recette.level,
        "metier": recette.metier_id,
        "ingredients": [ingredient.pk for ingredient in ingredients]
    }
    assert actual_values == expected_values
