from config import Config
from sqlalchemy import create_engine
from models import Base
import os

config = Config()
database_uri = config.db_uri


def create_all_tables(database_uri: str):
    engine = create_engine(database_uri, echo=True)
    Base.metadata.create_all(engine)


def delete_all_tables(database_uri: str):
    engine = create_engine(database_uri)
    Base.metadata.drop_all(bind=engine)

if __name__ == '__main__':
    delete_all_tables(database_uri)
    create_all_tables(database_uri)