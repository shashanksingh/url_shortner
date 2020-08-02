import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    LongUrl,
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

    urls_to_shorten = {
        "https://medium.com/@efhello",
        "https://www.hello.ef.com",
        "https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91",
        "https://www.youtube.com/watch?v=IqiTJK_uzUY",
        "https://earthengine.google.com/timelapse/#v=37.79184,-122.33478,12.026,"
        "latLng&t=1.73&ps=50&bt=19840101&et=2018123 1&startDwell=0&endDwell=0 ",
        "https://earthengine.google.com/timelapse/#v=37.79184,-122.33478,12.026,"
        "latLng&t=1.73&ps=50&bt=19840101&et=20181231&startDwell=0&endDwell=0 ",
        "https://en.wikipedia.org/wiki/Base64",
    }
    for url in urls_to_shorten:
        request = LongUrl(url=url)
        response = stub.create_short_url(request)
        print(f"url={url} => \n{response}")

except grpc._channel._InactiveRpcError:
    print("URL Shortner service is down")
