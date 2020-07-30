from google.protobuf.timestamp_pb2 import Timestamp

from src.generated.url_shortner_service_pb2 import Pong, Status, Success, ShortUrl
from src.generated.url_shortner_service_pb2_grpc import UrlShortnerServiceServicer


class UrlShortnerServiceServicerProxy(UrlShortnerServiceServicer):
    def __init__(self):
        pass

    def ping(self, request, context):
        return Pong(message="Open the POD BAY ! HAL")

    def create_short_url(self, request, context):
        timestamp = Timestamp()
        return ShortUrl(
            short_url="https://domain_name/qwerty",
            error=None,
            success=Success(code_number=Success.Code.ALL_GOOD, message=None),
        )

    def get_short_url_details(self, request, context):
        pass

    def get_all_short_urls(self, request, context):
        pass
