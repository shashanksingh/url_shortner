import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import (
    Empty,
    ShortUrl,
)

from flask import Flask,redirect
from markupsafe import escape
from src.constants import Constants

#initlizations
app = Flask(__name__)
channel = grpc.insecure_channel(f"localhost:{Constants.PORT_EXPOSED}")
grpc_stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)


#redirection route
@app.route('/<short_url>')
def redirector(short_url):
    request = ShortUrl(escape(short_url))
    grpc_stub.get_short_url_details(request)
    return redirect(grpc_stub.long_url, code=302)


