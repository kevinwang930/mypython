from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, MetaData)
engine = create_engine(
    "mysql+pymysql://kevin:123456@localhost:3306/orderdb")
meta = MetaData()
meta.reflect(bind=engine)
for table in meta.tables:
    print(table)