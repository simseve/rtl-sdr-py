from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = Config()
database_uri = config.db_uri

# Create the engine
engine = create_engine(database_uri, echo=True)

# Create the Session class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# def get_db():
#     session = Session()
#     try:
#         yield session
#     finally:
#         session.close()