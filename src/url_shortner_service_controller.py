from google.protobuf.timestamp_pb2 import Timestamp

from src.common.hashing import hashing_function
from src.generated.url_shortner_service_pb2 import (
    Pong,
    ShortUrl,
    ShortUrlDetails,
    ListOfShortUrlDetails,
    Error,
    Success,
)
from src.generated.url_shortner_service_pb2_grpc import UrlShortnerServiceServicer
from constants import Constants
from src.database.orm import Orm
from src.common.exceptions import DatabaseException, ValidationException


class UrlShortnerServiceController(UrlShortnerServiceServicer):
    def __init__(self):
        self.orm = Orm()

    def ping(self, request, context):
        return Pong(message=Constants.OPEN_THE_POD_BAY_DOOR)

    def create_short_url(self, request, context):
        error_message = None
        db_response = None
        short_url = None
        try:
            short_url = self.orm.create_short_url(long_url=request)
        except DatabaseException as e:
            error_message = str(e)
        except ValidationException as e:
            error_message = "Validation Error in input"

        if not error_message:
            return ShortUrl(
                short_url=short_url,
                error=None,
                success=Success(code_number=None, message=short_url),
            )
        return ShortUrl(
            short_url=None,
            error=Error(code_number=Error.Code.Failed, message=error_message),
            success=None,
        )

    def get_short_url_details(self, request, context):
        error_message = None
        response = ListOfShortUrlDetails()
        try:
            db_response = self.orm.get_short_url_details(short_url=request)
        except DatabaseException as e:
            error_message = str(e)
        except ValidationException as e:
            error_message = "Validation Error in input"

        if error_message:
            response.list_of_short_urls.extend[
                ShortUrlDetails(short_url=None, long_url=None, created_at=None)
            ]
            response.error = Error()
            response.success = None
        else:
            response.list_of_short_urls.extend(
                [
                    ShortUrlDetails(
                        short_url=item[0], long_url=item[1], created_at=item[2]
                    )
                    for item in db_response
                ]
            )
            response.error = None
            response.success = Success()
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
