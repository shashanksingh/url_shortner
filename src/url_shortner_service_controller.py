from google.protobuf.timestamp_pb2 import Timestamp

from src.generated.url_shortner_service_pb2 import (
    Pong,
    Success,
    ShortUrl,
    ShortUrlDetails,
    ListOfShortUrlDetails,
)
from src.generated.url_shortner_service_pb2_grpc import UrlShortnerServiceServicer


class UrlShortnerServiceServicerController(UrlShortnerServiceServicer):
    def __init__(self):
        pass

    def ping(self, request, context):
        return Pong(message="Open the POD BAY ! HAL")

    def create_short_url(self, request, context):
        return ShortUrl(
            short_url="https://domain_name/qwerty",
            error=None,
            success=Success(code_number=Success.Code.ALL_GOOD, message=None),
        )

    def get_short_url_details(self, request, context):
        timestamp = Timestamp()
        response = ListOfShortUrlDetails()
        response.list_of_short_urls.extend(
            [
                ShortUrlDetails(
                    short_url="https://domain_name/qwerty",
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
                    short_url="https://domain_name/qwerty",
                    created_at=timestamp.GetCurrentTime(),
                )
            ]
        )
        return response
