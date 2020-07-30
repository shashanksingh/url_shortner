# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

# imports for functionality
# from src.undirected import Undirected

# for Emojis in logs
import emoji

# imports for the server
import grpc
from src.generated.url_shortner_service_pb2_grpc import (
    add_UrlShortnerServiceServicer_to_server,
)
from src.url_shortner_service_controller import UrlShortnerServiceServicerController

from concurrent import futures
from src.Constants import Constants


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=Constants.MAX_WORKERS_FOR_SERVER)
    )
    add_UrlShortnerServiceServicer_to_server(
        UrlShortnerServiceServicerController(), server
    )
    server.add_insecure_port(f"[::]:{Constants.PORT_EXPOSED}")
    print(emoji.emojize(Constants.ALL_SYSTEMS_GO))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print(emoji.emojize(Constants.RUNNING_ON_PORT))
    serve()
