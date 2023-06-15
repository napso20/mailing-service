from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostOffice(Base):
    __tablename__ = 'post_office'

    post_office_id = Column('pot_office_id', VARCHAR(225), nullable=False, primary_key=True)
    address = Column('address', VARCHAR(512), nullable=False)
    zip_code = Column('zip_code', VARCHAR(255), nullable=True)
    name = Column('name', VARCHAR(255), nullable=False)

    packages = relationship('Package', backref='post_office', lazy=True)
