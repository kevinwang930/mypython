
from sqlalchemy import create_engine, MetaData, engine_from_config

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
eng = create_engine(
    "mysql+pymysql://kevin:123456@localhost:3306/orderdb")


Base = declarative_base()


class Car(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)


Session = sessionmaker(bind=eng)
ses = Session()

rs = ses.query(Car).filter(Car.Id.in_([2, 4, 6, 8]))

for car in rs:
    print (car.Id, car.Name, car.Price)
