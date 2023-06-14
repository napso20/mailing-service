import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_username = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
engine = create_engine(f'postgresql://{db_username}:{db_password}@localhost:5432/{db_name}')
Session = sessionmaker(bind=engine)

# Import the model classes
from .package import Package
from .post_office import PostOffice
from .package_status import PackageStatus

__all__ = [
    'Session',
    'Package',
    'PostOffice',
    'PackageStatus'
]
