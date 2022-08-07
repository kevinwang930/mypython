from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine
from project.app_logger import logger
from sqlalchemy.sql import text
engine = create_engine(
    "mysql+pymysql://kevin:123456@localhost:3306/orderdb")
Base = declarative_base()

with engine.connect() as con:
    rs = con.execute('select englishname from supplier where supplierNo = 100')
    logger.info(f'rs is {rs.keys()}')
    data = rs.fetchone()
    logger.info(data)

    con.execute('CREATE TABLE if not exists test_Cars(Id INTEGER PRIMARY KEY,Name TEXT, Price INTEGER)')

    data = ({"Id": 1, "Name": "Audi", "Price": 52642},
            {"Id": 2, "Name": "Mercedes", "Price": 57127},
            {"Id": 3, "Name": "Skoda", "Price": 9000},
            {"Id": 4, "Name": "Volvo", "Price": 29000},
            {"Id": 5, "Name": "Bentley", "Price": 350000},
            {"Id": 6, "Name": "Citroen", "Price": 21000},
            {"Id": 7, "Name": "Hummer", "Price": 41400},
            {"Id": 8, "Name": "Volkswagen", "Price": 21600}
            )

    for line in data:
        con.execute(text('insert into test_cars (Id,Name,Price) values(:Id,:Name,:Price)'),**line)



