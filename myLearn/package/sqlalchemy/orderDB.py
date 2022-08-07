
from sqlalchemy import create_engine, Column, Integer, String,Date,MetaData,engine_from_config, ForeignKey,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.mysql import FLOAT
Base = declarative_base()


class DB_supplier(Base):
    __tablename__ = "supplier"
    Id = Column(Integer, autoincrement = True,primary_key=True)
    englishName = Column(String(80),unique = True)
    chineseName = Column(String(40),unique = True)
    address = Column(String(100))
    paymentTerms = Column(String(40))
    contacts = relationship("contact")

class DB_contact(Base):
    __tablename__ = "contact"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    supplierId = Column(Integer, ForeignKey("supplier.Id",onupdate="cascade",ondelete="cascade"))
    name = Column(String(40))
    phone = Column(String(40))
    email = Column(String(40))
    from_date = Column(Date,server_default = func.current_date())
    to_date = Column(Date, default=None)

class DB_order(Base):
    __tablename__ = "order"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    supplierId = Column(Integer, ForeignKey(
        "supplier.Id", onupdate="cascade", ondelete="cascade"))
    date = Column(Date, server_default=func.current_date())
    volumn = Column(FLOAT(scale = 2), default = None)
    grossWeight = Column(FLOAT(scale=2), default=None)
    netWeight = Column(FLOAT(scale=2), default=None)
    amount = Column(FLOAT(scale=2), default=None)
    paymentMethod = Column(String(40))
    deliveryTerms = Column(String(40))




# Session = sessionmaker(bind=eng)
# ses = Session()
# res = ses.query(supplier).filter(supplier.Id == 100).first()
# if res:
#     print(res.contacts)


def initDB(dbName):
    eng = create_engine(
        "mysql+pymysql://kevin:123456@localhost:3306")

    with eng.connect() as con:
        con.execute('drop database if exists test')
        con.execute(f'create database {dbName}')
    print(f'database {dbName} recreated')

    eng = create_engine(
        f"mysql+pymysql://kevin:123456@localhost:3306/{dbName}")
    Base.metadata.bind = eng
    # Base.metadata.drop_all()
    Base.metadata.create_all()
    print(f'tables created {Base.metadata.tables.keys()}')

   
initDB('test')     
 
