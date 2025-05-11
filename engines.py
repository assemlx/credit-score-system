from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URIS

engines = {name: create_engine(uri) for name, uri in DB_URIS.items()}
Sessions = {name: sessionmaker(bind=engine) for name, engine in engines.items()}