from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostOffice(Base):
    __tablename__ = 'post_office'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    zip_code = Column(String)
    name = Column(String)

    packages = relationship('Package', backref='post_office', lazy=True)
