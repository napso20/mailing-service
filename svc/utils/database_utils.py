import os


def create_db_connection_url():
    db_username = os.environ.get('POSTGRES_USER')
    db_password = os.environ.get('POSTGRES_PASSWORD')
    db_name = os.environ.get('POSTGRES_DB')
    db_host = os.environ.get('PGHOST')
    db_port = os.environ.get('PGPORT', '5432')
    db_connection_url = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    return db_connection_url
