from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from src.common.singleton import Singleton
from constants import Constants
from src.common.hashing import hashing_function


class Orm(metaclass=Singleton):
    """
    A singleton class to access data from database
    """

    def __init__(self):
        engine_string = "mysql+mysqldb:///"
        engine_string += f"{Constants.MYSQL_USER_NAME}:{Constants.MYSQL_PASSWORD}"
        engine_string += f"@{Constants.MYSQL_HOST}/{Constants.MYSQL_DB}?host=localhost?port=3306"
        self._engine = create_engine('mysql+mysqldb://user:password@127.0.0.1/db', echo=True,)
        session_object = sessionmaker(bind=self._engine)

        base = automap_base()
        base.prepare(self._engine, reflect=True)
        self.session = session_object()
        self.models = base.classes
        self.url = base.classes.Urls

    def create_short_url(self, long_url:str ) -> bool:
        try:
            url = self.url(long_url=long_url, short_url=hashing_function(long_url))
            self.session.add(url)
            self.session.commit()
        except IntegrityError as e:
            print("Duplicate items being inserted")
