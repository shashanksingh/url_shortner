import random
import string

import sqlalchemy

from src.database.orm import Orm
from testcontainers.mysql import MySqlContainer


def random_character():
    return random.choice(string.ascii_lowercase)


def save_all_into_storage():
    with MySqlContainer("mysql:8.0.21") as mysql:
        engine = sqlalchemy.create_engine(mysql.get_connection_url())
        orm = Orm(engine=engine)
        orm.create_short_url(long_url=f"HTTP://MOCK_URL/{random_character()}")


def test_performance_of_saving_all_graphs_into_storage(benchmark):
    benchmark(save_all_into_storage)
