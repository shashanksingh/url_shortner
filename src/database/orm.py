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
from src.common.hashing import generate_short_url, generate_unique_hash


class Orm(metaclass=Singleton):
    """
    A singleton class to access data from database
    """

    def __init__(self, engine=None):
        """

        :param engine: A side effect which would be removed in future
        """
        if not engine:
            self._engine = create_engine(
                f"{Constants.MYSQL_PROTOCOL}://{Constants.MYSQL_USER_NAME}:{Constants.MYSQL_PASSWORD}@"
                f"{Constants.MYSQL_HOST}/{Constants.MYSQL_DB}",
                echo=True,
            )
        else:
            self._engine = engine
        session_object = sessionmaker(bind=self._engine)

        base = automap_base()
        base.prepare(self._engine, reflect=True)
        self.session = session_object()
        self.models = base.classes
        self.url = base.classes.Urls

    def create_short_url(self, long_url: str) -> str:
        """
        uses uuid function and creates long url
        :param long_url: get the long url
        :return: sshort url
        """
        if not long_url:
            raise ValidationException()

        try:
            url_object = self.get_long_url_details(long_url)
            if url_object and len(url_object) > 0:
                short_url = url_object[0][0]
            else:
                short_url = generate_short_url()
                self.session.add(
                    self.url(
                        long_url=long_url,
                        short_url=short_url,
                        long_url_hash=generate_unique_hash(long_url),
                    )
                )
                self.session.commit()
        except IntegrityError as e:
            raise DatabaseException()
        except OperationalError as e:
            raise DatabaseException()
        return short_url

    def get_short_url_details(self, short_url: str) -> List[Tuple]:
        """
        get details of specific short url
        :param short_url: find ll details of short_url
        :return: List of the tho points short_url and long url
        """
        if not short_url:
            raise ValidationException()
        try:
            url_objects = (
                self.session.query(self.url).filter_by(short_url=short_url).all()
            )
        except IntegrityError as e:
            raise FieldAlreadyExists()
        except OperationalError as e:
            raise DatabaseException()
        return [
            (url_object.short_url, url_object.long_url) for url_object in url_objects
        ]

    def get_all_short_urls(self) -> List[Tuple]:
        """
        get all short urls
        :return: List of Short url details
        """
        try:
            url_objects = self.session.query(self.url).all()
        except IntegrityError as e:
            raise FieldAlreadyExists()
        except OperationalError as e:
            raise DatabaseException()
        return [
            (url_object.short_url, url_object.long_url) for url_object in url_objects
        ]

    def get_long_url_details(self, long_url: str) -> List[Tuple]:
        """
        Used by create_short_url to see if  short url alresdy exists for specific long url
        :param long_url:
        :return: short url tuple
        """
        try:
            url_objects = (
                self.session.query(self.url)
                .filter_by(long_url_hash=generate_unique_hash(long_url))
                .all()
            )
        except OperationalError as e:
            raise DatabaseException()
        return [
            (url_object.short_url, url_object.long_url) for url_object in url_objects
        ]
