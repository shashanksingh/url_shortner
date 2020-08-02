from typing import List, Tuple

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from src.common.exceptions import (
    DatabaseException,
    ValidationException,
    FieldAlreadyExists,
)
from src.common.singleton import Singleton
from constants import Constants
from src.common.hashing import hashing_function


class Orm(metaclass=Singleton):
    """
    A singleton class to access data from database
    """

    def __init__(self):
        self._engine = create_engine(
            f"{Constants.MYSQL_PROTOCOL}://{Constants.MYSQL_USER_NAME}:{Constants.MYSQL_PASSWORD}@"
            f"{Constants.MYSQL_HOST}/{Constants.MYSQL_DB}",
            echo=True,
        )
        session_object = sessionmaker(bind=self._engine)

        base = automap_base()
        base.prepare(self._engine, reflect=True)
        self.session = session_object()
        self.models = base.classes
        self.url = base.classes.Urls

    def create_short_url(self, long_url: str) -> str:
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
        return short_url

    def get_short_url_details(self, short_url: str) -> List[Tuple]:
        if not short_url:
            raise ValidationException()
        short_url = hashing_function(short_url)
        try:
            url_objects = self.session.query(self.url).filter_by(short_url=short_url).all()
        except IntegrityError as e:
            raise FieldAlreadyExists()
        except OperationalError as e:
            raise DatabaseException()
        return [
            (url_object.short_url, url_objects.long_url, url_objects.created_at,)
            for url_object in url_objects
        ]
