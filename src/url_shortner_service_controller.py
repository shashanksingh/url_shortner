from google.protobuf.timestamp_pb2 import Timestamp

from src.common.hashing import hashing_function
from src.generated.url_shortner_service_pb2 import (
    Pong,
    ShortUrl,
    ShortUrlDetails,
    ListOfShortUrlDetails,
    Error,
)
from src.generated.url_shortner_service_pb2_grpc import UrlShortnerServiceServicer
from constants import Constants
from src.database.orm import Orm
from src.common.exceptions import DatabaseException, ValidationException


class UrlShortnerServiceServicerController(UrlShortnerServiceServicer):
    def __init__(self):
        self.orm = Orm()

    def ping(self, request, context):
        return Pong(message=Constants.OPEN_THE_POD_BAY_DOOR)

    def create_short_url(self, request, context):
        error_message = None
        response = None
        short_url = None
        try:
            response, short_url = self.orm.create_short_url(long_url=request)
        except DatabaseException as e:
            error_message = str(e)
        except ValidationException as e:
            error_message = "Validation Error in input"

        if response:
            return ShortUrl(short_url=short_url)
        return ShortUrl(
            short_url=None,
            error=Error(code_number=None, message=error_message),
            success=None,
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
