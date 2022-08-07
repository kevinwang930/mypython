from sqlalchemy import (create_engine, inspect)
engine = create_engine(
    "mysql+pymysql://kevin:123456@localhost:3306/orderdb")


insp = inspect(engine)
print (insp.get_table_names())
print (insp.get_columns("test_Cars"))
print (insp.get_primary_keys("test_Cars"))
print(insp.get_pk_constraint('test_Cars'))
print (insp.get_schema_names())
