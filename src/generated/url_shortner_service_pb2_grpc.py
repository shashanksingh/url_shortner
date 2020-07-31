# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import url_shortner_service_pb2 as url__shortner__service__pb2


class UrlShortnerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/UrlShortnerService/ping',
                request_serializer=url__shortner__service__pb2.Empty.SerializeToString,
                response_deserializer=url__shortner__service__pb2.Pong.FromString,
                )
        self.create_short_url = channel.unary_unary(
                '/UrlShortnerService/create_short_url',
                request_serializer=url__shortner__service__pb2.LongUrl.SerializeToString,
                response_deserializer=url__shortner__service__pb2.ShortUrl.FromString,
                )
        self.get_short_url_details = channel.unary_unary(
                '/UrlShortnerService/get_short_url_details',
                request_serializer=url__shortner__service__pb2.ShortUrl.SerializeToString,
                response_deserializer=url__shortner__service__pb2.ListOfShortUrlDetails.FromString,
                )
        self.get_all_short_urls = channel.unary_unary(
                '/UrlShortnerService/get_all_short_urls',
                request_serializer=url__shortner__service__pb2.Empty.SerializeToString,
                response_deserializer=url__shortner__service__pb2.ListOfShortUrlDetails.FromString,
                )


class UrlShortnerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_short_url(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_short_url_details(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all_short_urls(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UrlShortnerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=url__shortner__service__pb2.Empty.FromString,
                    response_serializer=url__shortner__service__pb2.Pong.SerializeToString,
            ),
            'create_short_url': grpc.unary_unary_rpc_method_handler(
                    servicer.create_short_url,
                    request_deserializer=url__shortner__service__pb2.LongUrl.FromString,
                    response_serializer=url__shortner__service__pb2.ShortUrl.SerializeToString,
            ),
            'get_short_url_details': grpc.unary_unary_rpc_method_handler(
                    servicer.get_short_url_details,
                    request_deserializer=url__shortner__service__pb2.ShortUrl.FromString,
                    response_serializer=url__shortner__service__pb2.ListOfShortUrlDetails.SerializeToString,
            ),
            'get_all_short_urls': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all_short_urls,
                    request_deserializer=url__shortner__service__pb2.Empty.FromString,
                    response_serializer=url__shortner__service__pb2.ListOfShortUrlDetails.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UrlShortnerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UrlShortnerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UrlShortnerService/ping',
            url__shortner__service__pb2.Empty.SerializeToString,
            url__shortner__service__pb2.Pong.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_short_url(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UrlShortnerService/create_short_url',
            url__shortner__service__pb2.LongUrl.SerializeToString,
            url__shortner__service__pb2.ShortUrl.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_short_url_details(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UrlShortnerService/get_short_url_details',
            url__shortner__service__pb2.ShortUrl.SerializeToString,
            url__shortner__service__pb2.ListOfShortUrlDetails.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all_short_urls(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UrlShortnerService/get_all_short_urls',
            url__shortner__service__pb2.Empty.SerializeToString,
            url__shortner__service__pb2.ListOfShortUrlDetails.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
