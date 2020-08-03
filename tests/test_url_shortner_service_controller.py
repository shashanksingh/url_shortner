import sqlalchemy

from src.database.orm import Orm
from src.generated.url_shortner_service_pb2 import LongUrl
from src.url_shortner_service_controller import UrlShortnerServiceController
from testcontainers.mysql import MySqlContainer


def test_create_short_url(mocker):
    with MySqlContainer("mysql:8.0.21") as mysql:
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        orm = Orm(engine=engine)
        mocker.patch("src.database.orm", return_value=orm)
        shortner = UrlShortnerServiceController()
        shortner.create_short_url(request=LongUrl(url="https://MOCKURL"), context=None)
        assert orm.assert_called_once_with("https://MOCKURL")


def test_get_short_url_details(mocker):
    with MySqlContainer("mysql:8.0.21") as mysql:
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        orm = Orm(engine=engine)
        mocker.patch("src.database.orm", return_value=orm)
        shortner = UrlShortnerServiceController()
        shortner.get_short_url_details(
            request=LongUrl(url="https://MOCKURL"), context=None
        )
        assert orm.assert_called_once_with("https://MOCKURL")


def test_get_all_short_urls(mocker):
    with MySqlContainer("mysql:8.0.21") as mysql:
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        orm = Orm(engine=engine)
        mocker.patch("src.database.orm", return_value=orm)
        shortner = UrlShortnerServiceController()
        shortner.create_short_url(request=LongUrl(url="https://MOCKURL"), context=None)
        assert orm.assert_called_once_with("https://MOCKURL")
