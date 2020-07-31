from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from typing import List

Base = declarative_base()


class Url(Base):
    __tablename__ = "Urls"
    id = Column(Integer, primary_key=True)
    long_url = Column(String, index=True)
    short_url = Column(String)
    created_at = Column(Integer)

    def get_long_url(self, short_url: str) -> List[str]:
        return self.long_url_url

    def create_short_url(self, long_url: str) -> List[str]:
        # function to convert to hash
        # store in db
        # return the shrot url
        return ""

    def get_all_short_url(self) -> List[str]:
        return []

    def __repr__(self):
        return "<URl (title='{}', short_url='{}', created_at={})>".format(
            self.long_url, self.short_url, self.created_at
        )
