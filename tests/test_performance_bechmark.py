import random
import string

import sqlalchemy

from src.database.orm import Orm
from testcontainers.mysql import MySqlContainer


def random_character():
    return random.choice(string.ascii_lowercase)


def save_all_into_storage(engine):
    orm = Orm(engine=engine)
    orm.create_short_url(long_url=f"HTTP://MOCK_URL/{random_character()}")


# def test_performance(benchmark):
#     with MySqlContainer("mysql:5.7.28") as mysql:
#         engine = sqlalchemy.create_engine(mysql.get_connection_url())
#         try:
#             engine.execute(
#                 """
#                 CREATE TABLE IF NOT EXISTS Urls (
#                     `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
#                     `long_url` varchar(2048) NOT NULL,
#                     `short_url` varchar(255) NOT NULL,
#                     `created_at` Timestamp DEFAULT CURRENT_TIMESTAMP,
#                     `long_url_hash` varchar(512) NOT NULL, /* To enforce one long url is one short url*/
#                     PRIMARY KEY (`id`),
#                     UNIQUE INDEX long_url_hash_uniqueness_constraint (long_url_hash)
#                 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#             """
#             )
#         except sqlalchemy.exc.InvalidRequestError:
#             pass
#         benchmark(save_all_into_storage, engine)
