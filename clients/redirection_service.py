import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import ShortUrl

from flask import Flask, redirect
from markupsafe import escape
from constants import Constants

# initializations
app = Flask(__name__, template_folder="templates")
channel = grpc.insecure_channel(f"localhost:{Constants.API_PORT_EXPOSED}")
grpc_stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)


# redirection route
@app.route("/")
def index():
    return Constants.OOPS_SOMETHING_WENT_WRONG


@app.route("/<short_url>")
def redirect_service(short_url: str):
    if short_url:
        request = ShortUrl(short_url=escape(short_url))
        response = grpc_stub.get_short_url_details(request)
        if response.list_of_short_urls and len(response.list_of_short_urls) == 1:
            return redirect(
                location=response.list_of_short_urls[0].long_url,
                code=Constants.HTTP_RESPONSE_CODE_FOR_PERMANENTLY_MOVED,
            )
    return Constants.OOPS_SOMETHING_WENT_WRONG


app.run(host="0.0.0.0", port=Constants.REDIRECT_PORT_EXPOSED)
