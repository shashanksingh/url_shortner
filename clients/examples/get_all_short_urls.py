import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    ShortUrl,
)

from constants import Constants

try:
    # open a gRPC channel
    channel = grpc.insecure_channel(f"localhost:{Constants.API_PORT_EXPOSED}")

    # create a stub (client)
    stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)

    # make the call
    response = stub.ping(Empty())
    print(response)

    request = ShortUrl()
    response = stub.get_all_short_urls(request)
    print(response)

except grpc._channel._InactiveRpcError:
    print("URL Shortner service is down")
