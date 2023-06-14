from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Package(Base):
    __tablename__ = 'package'

    id = Column(Integer, primary_key=True)
    destination_address = Column(String)
    destination_zip_code = Column(String)
    recipient_name = Column(String)
    type = Column(String)

    post_office_id = Column(Integer, ForeignKey('post_office.id'))
    status_history = relationship('PackageStatus', backref='package', lazy=True)
