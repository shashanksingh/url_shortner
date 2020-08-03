import sqlalchemy

from src.database.orm import Orm
from src.generated.url_shortner_service_pb2 import LongUrl
from src.url_shortner_service_controller import UrlShortnerServiceController
from testcontainers.mysql import MySqlContainer


# def test_create_short_url(mocker):
#     with MySqlContainer("mysql:5.7.28") as mysql:
#         engine = sqlalchemy.create_engine(mysql.get_connection_url())
#         engine.execute(
#             """
#             CREATE TABLE Urls (
#                 `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
#                 `long_url` varchar(2048) NOT NULL,
#                 `short_url` varchar(255) NOT NULL,
#                 `created_at` Timestamp DEFAULT CURRENT_TIMESTAMP,
#                 `long_url_hash` varchar(512) NOT NULL, /* To enforce one long url is one short url*/
#                 PRIMARY KEY (`id`),
#                 UNIQUE INDEX long_url_hash_uniqueness_constraint (long_url_hash) USING HASH
#             ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#         """
#         )
#         orm = Orm(engine=engine)
#         shortner = UrlShortnerServiceController()
#         shortner.create_short_url(request=LongUrl(url="https://MOCKURL"), context=None)
#         assert orm.get_all_short_urls()[0][1] == "https://MOCKURL"


# def test_get_short_url_details(mocker):
#     with MySqlContainer("mysql:5.7.28") as mysql:
#         engine = sqlalchemy.create_engine(mysql.get_connection_url())
#         engine.execute("""
#             CREATE TABLE Urls (
#                 `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
#                 `long_url` varchar(2048) NOT NULL,
#                 `short_url` varchar(255) NOT NULL,
#                 `created_at` Timestamp DEFAULT CURRENT_TIMESTAMP,
#                 `long_url_hash` varchar(512) NOT NULL, /* To enforce one long url is one short url*/
#                 PRIMARY KEY (`id`),
#                 UNIQUE INDEX long_url_hash_uniqueness_constraint (long_url_hash) USING HASH
#             ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#         """)
#         orm = Orm(engine=engine)
#         shortner = UrlShortnerServiceController()
#         shortner.get(request=LongUrl(url="https://MOCKURL"), context=None)
#         assert orm.get_all_short_urls()[0][1] == "https://MOCKURL"


def test_get_all_short_urls():
    with MySqlContainer("mysql:5.7.28") as mysql:
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        engine.execute(
            """
            CREATE TABLE Urls (
                `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
                `long_url` varchar(2048) NOT NULL,
                `short_url` varchar(255) NOT NULL,
                `created_at` Timestamp DEFAULT CURRENT_TIMESTAMP,
                `long_url_hash` varchar(512) NOT NULL, /* To enforce one long url is one short url*/
                PRIMARY KEY (`id`),
                UNIQUE INDEX long_url_hash_uniqueness_constraint (long_url_hash)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        )
        orm = Orm(engine=engine)
        shortner = UrlShortnerServiceController()
        shortner.create_short_url(
            request=LongUrl(url="https://MOCKURLONE"), context=None
        )
        shortner.create_short_url(
            request=LongUrl(url="https://MOCKURLTWO"), context=None
        )

        assert [x[1] for x in orm.get_all_short_urls()].sort() == [
            "https://MOCKURLONE",
            "https://MOCKURLTWO",
        ].sort()
        assert len(orm.get_all_short_urls()) == 2
