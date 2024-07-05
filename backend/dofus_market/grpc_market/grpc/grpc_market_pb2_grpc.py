# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from grpc_market.grpc import grpc_market_pb2 as grpc__market__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in grpc_market_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class IngredientControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/dofus_market.grpc_market.IngredientController/Create',
                request_serializer=grpc__market__pb2.IngredientRequest.SerializeToString,
                response_deserializer=grpc__market__pb2.IngredientResponse.FromString,
                _registered_method=True)
        self.Destroy = channel.unary_unary(
                '/dofus_market.grpc_market.IngredientController/Destroy',
                request_serializer=grpc__market__pb2.IngredientDestroyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/dofus_market.grpc_market.IngredientController/List',
                request_serializer=grpc__market__pb2.IngredientListRequest.SerializeToString,
                response_deserializer=grpc__market__pb2.IngredientListResponse.FromString,
                _registered_method=True)
        self.PartialUpdate = channel.unary_unary(
                '/dofus_market.grpc_market.IngredientController/PartialUpdate',
                request_serializer=grpc__market__pb2.IngredientPartialUpdateRequest.SerializeToString,
                response_deserializer=grpc__market__pb2.IngredientResponse.FromString,
                _registered_method=True)
        self.Retrieve = channel.unary_unary(
                '/dofus_market.grpc_market.IngredientController/Retrieve',
                request_serializer=grpc__market__pb2.IngredientRetrieveRequest.SerializeToString,
                response_deserializer=grpc__market__pb2.IngredientResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/dofus_market.grpc_market.IngredientController/Update',
                request_serializer=grpc__market__pb2.IngredientRequest.SerializeToString,
                response_deserializer=grpc__market__pb2.IngredientResponse.FromString,
                _registered_method=True)


class IngredientControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartialUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IngredientControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=grpc__market__pb2.IngredientRequest.FromString,
                    response_serializer=grpc__market__pb2.IngredientResponse.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=grpc__market__pb2.IngredientDestroyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=grpc__market__pb2.IngredientListRequest.FromString,
                    response_serializer=grpc__market__pb2.IngredientListResponse.SerializeToString,
            ),
            'PartialUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.PartialUpdate,
                    request_deserializer=grpc__market__pb2.IngredientPartialUpdateRequest.FromString,
                    response_serializer=grpc__market__pb2.IngredientResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=grpc__market__pb2.IngredientRetrieveRequest.FromString,
                    response_serializer=grpc__market__pb2.IngredientResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=grpc__market__pb2.IngredientRequest.FromString,
                    response_serializer=grpc__market__pb2.IngredientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dofus_market.grpc_market.IngredientController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('dofus_market.grpc_market.IngredientController', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class IngredientController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dofus_market.grpc_market.IngredientController/Create',
            grpc__market__pb2.IngredientRequest.SerializeToString,
            grpc__market__pb2.IngredientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dofus_market.grpc_market.IngredientController/Destroy',
            grpc__market__pb2.IngredientDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dofus_market.grpc_market.IngredientController/List',
            grpc__market__pb2.IngredientListRequest.SerializeToString,
            grpc__market__pb2.IngredientListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PartialUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dofus_market.grpc_market.IngredientController/PartialUpdate',
            grpc__market__pb2.IngredientPartialUpdateRequest.SerializeToString,
            grpc__market__pb2.IngredientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dofus_market.grpc_market.IngredientController/Retrieve',
            grpc__market__pb2.IngredientRetrieveRequest.SerializeToString,
            grpc__market__pb2.IngredientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/dofus_market.grpc_market.IngredientController/Update',
            grpc__market__pb2.IngredientRequest.SerializeToString,
            grpc__market__pb2.IngredientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
