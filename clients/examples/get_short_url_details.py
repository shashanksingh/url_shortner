import grpc
from src.generated import url_shortner_service_pb2, url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    LongUrl,
    ShortUrl,
)

from src.constants import Constants

# open a gRPC channel
channel = grpc.insecure_channel(f"localhost:{Constants.PORT_EXPOSED}")

# create a stub (client)
stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)


# make the call
response = stub.ping(Empty())
print(response)

# https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/

request = ShortUrl()
response = stub.get_short_url_details(request)
print(response)
