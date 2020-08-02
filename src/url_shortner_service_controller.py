from google.protobuf.timestamp_pb2 import Timestamp

from src.generated.url_shortner_service_pb2 import (
    Pong,
    Success,
    ShortUrl,
    ShortUrlDetails,
    ListOfShortUrlDetails, Error,
)
from src.generated.url_shortner_service_pb2_grpc import UrlShortnerServiceServicer
from constants import Constants
from src.database.orm import Orm
from src.common.hashing import hashing_function
from src.database.database_exception import DatabaseException

class UrlShortnerServiceServicerController(UrlShortnerServiceServicer):
    def __init__(self):
        self.orm = Orm()

    def ping(self, request, context):
        return Pong(message=Constants.OPEN_THE_POD_BAY_DOOR)

    def create_short_url(self, request, context):
        if request.long_url:
            try:
                new_url = self.orm.create_short_url(long_url=request.long_url)
                if new_url:
                    return ShortUrl(
                        short_url=f"{Constants.BASE_DOMAIN_FOR_REDIRECTION_SERVICE}/qwerty",
                        error=None,
                        success=Success(code_number=Success.Code.ALL_GOOD, message=None),
                    )
            except DatabaseException as e:
                pass

        return ShortUrl(
            short_url=None,
            error=Error(),
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
