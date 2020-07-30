import grpc
from src.generated import url_shortner_service_pb2, url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    LongUrl,
)

PORT_EXPOSED = 9090

# open a gRPC channel
channel = grpc.insecure_channel(f"localhost:{PORT_EXPOSED}")

# create a stub (client)
stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)


# make the call
response = stub.ping(Empty())
print(response)

# https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/

request = LongUrl(url="https://medium.com/@efhello",)
response = stub.create_short_url(request)
print(response)