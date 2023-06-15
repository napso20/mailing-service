from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PackageStatus(Base):
    __tablename__ = 'package_status'

    package_status_id = Column('package_status_id', VARCHAR(225), nullable=False, primary_key=True)
    package_id = Column('package_id', VARCHAR(255), nullable=False)
    status = Column('status', VARCHAR(255), nullable=True)
    timestamp = Column('timestamp', DateTime())

    package = relationship('Package', backref='status_history')
