from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PackageStatus(Base):
    __tablename__ = 'package_status'

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey('package.id'))
    status = Column(String)
    timestamp = Column(DateTime)

    package = relationship('Package', backref='status_history')
