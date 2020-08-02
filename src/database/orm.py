from typing import List

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from src.common.exceptions import DatabaseException
from src.common.singleton import Singleton
from constants import Constants
from src.common.hashing import hashing_function
from src.generated.url_shortner_service_pb2 import ShortUrlDetails


class Orm(metaclass=Singleton):
    """
    A singleton class to access data from database
    """

    def __init__(self):
        self._engine = create_engine(
            f"{Constants.MYSQL_PROTOCOL}://{Constants.MYSQL_USER_NAME}:{Constants.MYSQL_PASSWORD}@"
            f"{Constants.MYSQL_HOST}/{Constants.MYSQL_DB}", echo=True,
        )
        session_object = sessionmaker(bind=self._engine)

        base = automap_base()
        base.prepare(self._engine, reflect=True)
        self.session = session_object()
        self.models = base.classes
        self.url = base.classes.Urls

    def create_short_url(self, long_url: str) -> [bool, str]:
        short_url = hashing_function(long_url)
        try:
            self.session.add(
                self.url(long_url=long_url, short_url=hashing_function(long_url))
            )
            self.session.commit()
        except IntegrityError as e:
            raise DatabaseException()
        except OperationalError as e:
            raise DatabaseException()
        return True, short_url

    def get_short_url_details(self, short_url:str) -> List[ShortUrlDetails]:
        pass