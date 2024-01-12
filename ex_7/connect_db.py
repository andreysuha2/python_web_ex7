from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from ex_7.definitions import DB_CONNECTION_STRING

engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)
session = Session()