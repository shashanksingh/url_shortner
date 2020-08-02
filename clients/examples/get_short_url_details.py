import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    ShortUrl,
    LongUrl,
)
import emoji
from constants import Constants

try:
    # open a gRPC channel
    channel = grpc.insecure_channel(f"localhost:{Constants.API_PORT_EXPOSED}")

    # create a stub (client)
    stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)

    # create request
    urls_to_shorten = {
        "https://play.google.com/store/apps/details?id=com.ef.efhello&hl=en_GB",
    }
    response_of_create = None

    for url in urls_to_shorten:
        request = LongUrl(url=url)
        response_of_create = stub.create_short_url(request)
        print(
            emoji.emojize(
                f"🧐 Short URL created :  \n Url = {url} , \n Short URL = {response_of_create}"
            )
        )

    # ask for detail of same request
    request = ShortUrl(short_url=response_of_create.short_url)
    response = stub.get_short_url_details(request)
    print(
        emoji.emojize(
            f"🧐 Lets Request the newly created short link to get more details :"
            f"\n Short Link = {request} \n Details = {response}"
        )
    )

except grpc._channel._InactiveRpcError:
    print("URL Shortner service is down")
