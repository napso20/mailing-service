from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Package(Base):
    __tablename__ = 'package'

    package_id = Column('package_id', VARCHAR(225), nullable=False, primary_key=True)
    destination_address = Column('destination_address', VARCHAR(512), nullable=False)
    destination_zip_code = Column('destination_zip_code', VARCHAR(255), nullable=True)
    recipient_name = Column('recipient_name', VARCHAR(255), nullable=True)
    type = Column('type', VARCHAR(64), nullable=False)

    post_office_id = Column(Integer, ForeignKey('post_office.post_office_id'))
    status_history = relationship('PackageStatus', backref='package', lazy=True)
