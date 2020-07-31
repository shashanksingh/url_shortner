from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.models import Base, Url
from src.common.singleton import Singleton


class Orm(Singleton):
    """
    A singleton class to access data from database
    """

    def __init__(self):
        self.engine = create_engine("sqlite:///user:passwod@localhost", echo=True)
        session_object = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.session = session_object()

        url = Url(long_url="js", short_url="js")
        self.session.add(url)
