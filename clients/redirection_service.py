import grpc
from src.generated import url_shortner_service_pb2_grpc
from src.generated.url_shortner_service_pb2 import ShortUrl

from flask import Flask, redirect, render_template
from markupsafe import escape
from constants import Constants

# initializations
app = Flask(__name__)
channel = grpc.insecure_channel(f"localhost:{Constants.PORT_EXPOSED}")
grpc_stub = url_shortner_service_pb2_grpc.UrlShortnerServiceStub(channel)


# redirection route
@app.route("/")
@app.route("/<short_url>")
def index(short_url):
    if short_url:
        request = ShortUrl(short_url=escape(short_url))
        response = grpc_stub.get_short_url_details(request)
        if response.list_of_short_urls and len(response.list_of_short_urls) == 1:
            return redirect(response.list_of_short_urls[0].long_url, code=302)
    return render_template('index.html', requested_short_url = short_url)


app.run(host="0.0.0.0", port=5000)
