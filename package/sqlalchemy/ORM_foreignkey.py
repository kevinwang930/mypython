from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine(
    "mysql+pymysql://kevin:123456@localhost:3306/orderdb")

Base = declarative_base()


class supplier(Base):
    __tablename__ = "supplier"
    # supplierNo = Column(Integer, primary_key=True)
    # englishName = Column(String)
    # chinesename = Column(String)
    # contact = relationship("suppliercontact")


class suppliercontact(Base):
    __tablename__ = "suppliercontact"

    contactNo = Column(Integer, primary_key=True)
    # name = Column(String)

    # phone = Column(String)
    # email = Column(String)
    # supplierNo = Column(Integer, ForeignKey("supplier.supplierNo"))

    # supplier = relationship("supplier")


Session = sessionmaker(bind=eng)
ses = Session()

res = ses.query(supplier).filter(supplier.supplierNo == 1).first()

for contact in res.contact:
    print (contact.name)

res = ses.query(suppliercontact).filter(suppliercontact.name == "符小平").first()
print (res.supplier.englishName)
