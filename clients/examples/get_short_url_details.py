import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    ShortUrl,
)

from constants import Constants

# open a gRPC channel
channel = grpc.insecure_channel(f"localhost:{Constants.API_PORT_EXPOSED}")

# create a stub (client)
stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)


# make the call
response = stub.ping(Empty())
print(response)

# https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/

request = ShortUrl(short_url="79fd8c4c-195e-44f7-93b2-0ee98698cc7c")
response = stub.get_short_url_details(request)
print(response)
