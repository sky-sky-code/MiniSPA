from datetime import date
from sqlalchemy import Date, Integer, String, Column
from server.app.db.database import Base, engine

from server.app.db.database import Session

class SingleTable(Base):
    __tablename__ = "single_table"

    id = Column(String, primary_key=True)
    date_departure = Column(Date, default=date.today().strftime("%Y-%m-%d"))
    name_city = Column(String)
    quantity_human = Column(Integer)
    distance = Column(Integer)

Base.metadata.create_all(engine)
