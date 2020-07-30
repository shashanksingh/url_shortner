# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

# imports for functionality
# from src.undirected import Undirected

# for Emojis in logs
import emoji

# imports for the server
import grpc
from src.generated.url_shortner_service_pb2 import Pong, Status, Success
from src.generated.url_shortner_service_pb2_grpc import (
    UrlShortnerServiceServicer,
    add_UrlShortnerServiceServicer_to_server,
)
from src.generated import url_shortner_service_pb2 as url__shortner__service_pb2

import logging
from concurrent import futures

PORT_EXPOSED = 9090


class UrlShortnerServiceServicerProxy(UrlShortnerServiceServicer):
    def __init__(self):
        pass

    def ping(self, request, context):
        return Pong(message="ALl hail GRPC")

    def create_short_url(self, request, context):
        pass

    def get_short_url_details(self, request, context):
        pass

    def get_all_short_urls(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UrlShortnerServiceServicer_to_server(UrlShortnerServiceServicerProxy(), server)
    server.add_insecure_port(f"[::]:{PORT_EXPOSED}")
    print(emoji.emojize(f"All systems go :rocket:"))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    print(emoji.emojize(f"Running on port {PORT_EXPOSED} :thumbs_up:"))
    serve()
