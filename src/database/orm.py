from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from src.common.singleton import Singleton
from constants import Constants


class Orm(Singleton):
    """
    A singleton class to access data from database
    """

    def __init__(self):
        self.engine = create_engine(
            f"mysql:///{Constants.MYSQL_USER_NAME}:{Constants.MYSQL_PASSWORD}@{Constants.MYSQL_HOST}",
            echo=True,
        )
        session_object = sessionmaker(bind=self.engine)

        Base = automap_base()
        Base.prepare(self.engine, reflect=True)
        self.session = session_object()

        url_model = Base.classes.Url
        url = url_model(long_url="js", short_url="js")
        self.session.add(url)
