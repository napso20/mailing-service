from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..utils.database_utils import create_db_connection_url

db_connection_url = create_db_connection_url()
engine = create_engine(db_connection_url)
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
