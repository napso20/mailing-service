import os
# import socket
import sys

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy import MetaData

# Add the project directory to the Python path
sys.path.append(os.getcwd())

from svc.models import Package, PostOffice, PackageStatus

# Create the metadata object and reflect the models
target_metadata = MetaData()

# Alembic ini Config object
config = context.config

db_username = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_connection_url = f'postgresql://{db_username}:{db_password}@mail-service-db:5432/{db_name}'
print(f'....------ db_connection_url = {db_connection_url}')
# db_connection_url = "postgresql://postgres:password@" + socket.gethostbyname("mail-service-db") + "/mail-service-db"

# Set up the database connection
config.set_main_option('sqlalchemy.url', db_connection_url)

engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool
)

target_metadata.reflect(bind=engine)

# This hook function that is called for each migration script
def run_migrations_online():
    # Define the context with the configured connection and target metadata
    with context.begin_transaction():
        connection = context.connect()

        # Run the migrations
        context.configure(connection=connection, target_metadata=target_metadata)
        context.run_migrations()


run_migrations_online()
