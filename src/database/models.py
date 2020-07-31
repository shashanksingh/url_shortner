from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Url(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True)
    long_url = Column(String)
    short_url = Column(String)
    created_at = Column(Integer)

    def __repr__(self):
        return "<URl (title='{}', short_url='{}', created_at={})>".format(
            self.long_url, self.short_url, self.created_at
        )
