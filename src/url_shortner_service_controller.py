from google.protobuf.timestamp_pb2 import Timestamp

from src.generated.url_shortner_service_pb2 import (
    Pong,
    Success,
    ShortUrl,
    ShortUrlDetails,
    ListOfShortUrlDetails,
)
from src.generated.url_shortner_service_pb2_grpc import UrlShortnerServiceServicer
from constants import Constants
from src.database.models import Url


class UrlShortnerServiceServicerController(UrlShortnerServiceServicer):
    def __init__(self):
        pass

    def ping(self, request, context):
        return Pong(message=Constants.OPEN_THE_POD_BAY_DOOR)

    def create_short_url(self, request, context):
        if request.long_url:
            Url.create_short_url(long_url=request.long_url)
        return ShortUrl(
            short_url=f"{Constants.BASE_DOMAIN_FOR_REDIRECTION_SERVICE}/qwerty",
            error=None,
            success=Success(code_number=Success.Code.ALL_GOOD, message=None),
        )

    def get_short_url_details(self, request, context):
        timestamp = Timestamp()
        response = ListOfShortUrlDetails()
        response.list_of_short_urls.extend(
            [
                ShortUrlDetails(
                    long_url="https://www.hello.ef.com",
                    short_url=f"{Constants.BASE_DOMAIN_FOR_REDIRECTION_SERVICE}/qwerty",
                    created_at=timestamp.GetCurrentTime(),
                )
            ]
        )
        return response

    def get_all_short_urls(self, request, context):
        timestamp = Timestamp()
        response = ListOfShortUrlDetails()
        response.list_of_short_urls.extend(
            [
                ShortUrlDetails(
                    long_url="https://www.hello.ef.com",
                    short_url=f"{Constants.BASE_DOMAIN_FOR_REDIRECTION_SERVICE}/qwerty",
                    created_at=timestamp.GetCurrentTime(),
                )
            ]
        )
        return response
