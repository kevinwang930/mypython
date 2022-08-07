
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, MetaData,tuple_
from sqlalchemy.sql import select,and_,asc
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine(
    "mysql+pymysql://kevin:123456@localhost:3306/orderdb")

meta = MetaData(eng)
cars = Table('test_Cars', meta, autoload=True)
Session = sessionmaker(bind=eng)
ses = Session()
res = ses.query(cars).filter(cars.c.Price > 10000).first()
print(res)
    

# stm = select([cars.c.Name, cars.c.Price]).order_by(asc(cars.c.Name)).limit(3)
# rs = con.execute(stm)

# print (rs.fetchall())

# stm2 = select([cars.c.Name,cars.c.Price]).where(and_(cars.c.Price > 10000,cars.c.Price < 30000))
# rs = con.execute(stm2)
# print(rs.fetchall())

    # stm = select([cars]).where(cars.c.Name.like('%ent%'))
    # rs = con.execute(stm)
    # print (rs.fetchall())

    # k = [(2,),(4,),(6,),(7,)]
    # stm = select([cars]).where(tuple_(cars.c.Id).in_(k))
    # rs = con.execute(stm)
    # print(rs.fetchall())

