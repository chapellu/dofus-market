import grpc
import grpc_market.grpc.grpc_market_pb2 as pb2
import pytest
from django.test import TestCase, override_settings
from django_socio_grpc.tests.grpc_test_utils.fake_grpc import FakeFullAIOGRPC
from google.protobuf.empty_pb2 import Empty
from grpc_market.grpc.grpc_market_p2p import (RuneDestroyRequest,
                                              RuneListRequest,
                                              RuneListResponse, RuneRequest,
                                              RuneResponse,
                                              RuneRetrieveRequest)
from grpc_market.grpc.grpc_market_pb2_grpc import (
    RuneControllerStub, add_RuneControllerServicer_to_server)
from grpc_market.services.rune_service import RuneService
from market.database.rune import Rune


@override_settings(GRPC_FRAMEWORK={"GRPC_ASYNC": True})
class TestRune(TestCase):

    def setUp(self):
        self.fake_grpc = FakeFullAIOGRPC(
            add_RuneControllerServicer_to_server,
            RuneService.as_servicer(),
        )
        self.client: RuneControllerStub = self.fake_grpc.get_fake_stub(
            RuneControllerStub)

    def tearDown(self) -> None:
        self.fake_grpc.close()

    async def test__rune_to_string(self):
        # Given
        rune = Rune(name="Vitalité", prix_ba=10, prix_pa=100, prix_ra=100)

        # When
        string = str(rune)

        # Then
        self.assertEqual(string, "Vitalité")

    async def test__list_rune__empty_list__ok(self):
        # Given

        # When
        request = RuneListRequest()
        response: RuneListResponse = await self.client.List(request)

        # Then
        self.assertEqual(response.results, [])

    async def test__list_rune__list_with_2_items__ok(self):
        # Given
        runes = []
        runes.append(await Rune.objects.acreate(name="Force",
                                                prix_ba=20,
                                                prix_pa=200,
                                                prix_ra=200))
        runes.append(await Rune.objects.acreate(name="Vitalité",
                                                prix_ba=10,
                                                prix_pa=100,
                                                prix_ra=100))

        # When
        request = RuneListRequest()
        response: RuneListResponse = await self.client.List(request)

        # Then
        self.assertEqual(len(response.results), len(runes))
        for i in range(len(runes)):
            self.assertEqual(response.results[i].name, runes[i].name)
            self.assertEqual(response.results[i].prix_ba, runes[i].prix_ba)
            self.assertEqual(response.results[i].prix_pa, runes[i].prix_pa)
            self.assertEqual(response.results[i].prix_ra, runes[i].prix_ra)

    async def test__retrieve_rune__not_found(self):
        # Given
        rune_name = "Vitalité"

        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = RuneRetrieveRequest(name=rune_name)
            await self.client.Retrieve(request)

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.NOT_FOUND)
        self.assertEqual(
            expected_error.value.args[1].encode().decode('unicode_escape'),
            f'{{"message": "Rune: {rune_name} not found!", "code": "not_found"}}'
        )

    async def test__retrieve_rune__ok(self):
        # Given
        rune_name = "Vitalité"
        rune_prix_ba = 10
        rune_prix_pa = 100
        rune_prix_ra = 100
        await Rune.objects.acreate(name=rune_name,
                                   prix_ba=rune_prix_ba,
                                   prix_pa=rune_prix_pa,
                                   prix_ra=rune_prix_ra)
        # When
        request = RuneRetrieveRequest(name=rune_name)
        response: RuneResponse = await self.client.Retrieve(request)

        # Then
        self.assertEqual(response.name, rune_name)
        self.assertEqual(response.prix_ba, rune_prix_ba)
        self.assertEqual(response.prix_pa, rune_prix_ra)
        self.assertEqual(response.prix_ra, rune_prix_pa)

    async def test__create_rune__ok(self):
        # Given
        rune_name = "Vitalité"
        rune_prix_ba = 10
        rune_prix_pa = 100
        rune_prix_ra = 100

        # When
        request = RuneRequest(name=rune_name,
                              prix_ba=rune_prix_ba,
                              prix_pa=rune_prix_pa,
                              prix_ra=rune_prix_ra)
        response: RuneResponse = await self.client.Create(
            pb2.RuneRequest(**request.model_dump()))

        # Then
        self.assertEqual(response.name, rune_name)
        self.assertEqual(response.prix_ba, rune_prix_ba)
        self.assertEqual(response.prix_pa, rune_prix_ra)
        self.assertEqual(response.prix_ra, rune_prix_pa)
        rune = await Rune.objects.aget(name=rune_name)
        self.assertEqual(rune.name, rune_name)
        self.assertEqual(rune.prix_ba, rune_prix_ba)
        self.assertEqual(rune.prix_pa, rune_prix_ra)
        self.assertEqual(rune.prix_ra, rune_prix_pa)

    async def test__create_rune__already_exist(self):
        # Given
        rune_name = "Vitalité"
        rune_prix_ba = 10
        rune_prix_pa = 100
        rune_prix_ra = 100
        await Rune.objects.acreate(name=rune_name,
                                   prix_ba=rune_prix_ba,
                                   prix_pa=rune_prix_pa,
                                   prix_ra=rune_prix_ra)
        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = RuneRequest(name=rune_name,
                                  prix_ba=rune_prix_ba,
                                  prix_pa=rune_prix_pa,
                                  prix_ra=rune_prix_ra)
            response: RuneResponse = await self.client.Create(
                pb2.RuneRequest(**request.model_dump()))

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.INVALID_ARGUMENT)
        self.assertEqual(
            expected_error.value.args[1],
            '{"name": [{"message": "rune with this name already exists.", "code": "unique"}]}'
        )

    async def test__destroy_rune__ok(self):
        # Given
        rune_name = "Vitalité"
        rune_prix_ba = 10
        rune_prix_pa = 100
        rune_prix_ra = 100
        await Rune.objects.acreate(name=rune_name,
                                   prix_ba=rune_prix_ba,
                                   prix_pa=rune_prix_pa,
                                   prix_ra=rune_prix_ra)

        # When
        request = RuneDestroyRequest(name=rune_name)
        response: Empty = await self.client.Destroy(request)

        # Then
        self.assertTrue(isinstance(response, Empty))
        with pytest.raises(Rune.DoesNotExist):
            await Rune.objects.aget(name=rune_name)

    async def test__destroy_rune__does_not_exist(self):
        # Given
        rune_name = "Vitalité"

        # When
        with pytest.raises(grpc.RpcError) as expected_error:
            request = RuneDestroyRequest(name=rune_name)
            response: Empty = await self.client.Destroy(request)

        # Then
        self.assertEqual(expected_error.value.args[0],
                         grpc.StatusCode.NOT_FOUND)
        self.assertEqual(
            expected_error.value.args[1].encode().decode('unicode_escape'),
            f'{{"message": "Rune: {rune_name} not found!", "code": "not_found"}}'
        )

    async def test__update_rune__ok(self):
        # Given
        rune_name = "Vitalité"
        rune_prix_ba = 10
        rune_prix_pa = 100
        rune_prix_ra = 100
        await Rune.objects.acreate(name=rune_name,
                                   prix_ba=rune_prix_ba,
                                   prix_pa=rune_prix_pa,
                                   prix_ra=rune_prix_ra)

        # When
        request = RuneRequest(name=rune_name,
                              prix_ba=rune_prix_ba,
                              prix_pa=rune_prix_pa,
                              prix_ra=rune_prix_ra)
        response: RuneResponse = await self.client.Update(
            pb2.RuneRequest(**request.model_dump()))

        # Then
        self.assertEqual(response.name, rune_name)
        self.assertEqual(response.prix_ba, rune_prix_ba)
        self.assertEqual(response.prix_pa, rune_prix_ra)
        self.assertEqual(response.prix_ra, rune_prix_pa)
        rune = await Rune.objects.aget(name=rune_name)
        self.assertEqual(rune.name, rune_name)
        self.assertEqual(rune.prix_ba, rune_prix_ba)
        self.assertEqual(rune.prix_pa, rune_prix_ra)
        self.assertEqual(rune.prix_ra, rune_prix_pa)
