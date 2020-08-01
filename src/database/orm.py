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
        engine_string = "mysql+mysqldb:///"
        engine_string += f"{Constants.MYSQL_USER_NAME}:{Constants.MYSQL_PASSWORD}"
        engine_string += f"@{Constants.MYSQL_HOST}/{Constants.MYSQL_DB}?host=localhost?port=3306"
        self.engine = create_engine('mysql+mysqldb://user:password@127.0.0.1/db', echo=True,)
        session_object = sessionmaker(bind=self.engine)

        Base = automap_base()
        Base.prepare(self.engine, reflect=True)
        self.session = session_object()

        url_model = Base.classes.Url
        url = url_model(long_url="js", short_url="js")
        self.session.add(url)
