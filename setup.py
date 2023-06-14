from setuptools import setup, find_packages

setup(
    name='mailing-service',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'connexion',
        'werkzeug',
        'psycopg2-binary',
        'sqlalchemy',
        'alembic',
        # add other dependencies here
    ],
)
