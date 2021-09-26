from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from server import config

engine = create_engine(f'postgresql+psycopg2://postgres:{config.password}@localhost:5432/{config.name_database}',
                       echo=False)

Session = sessionmaker(bind=engine)

Base = declarative_base()

