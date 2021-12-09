"""
Loading csv data using pandas module.
"""
import pandas
from sqlalchemy import (Column, Integer, String, DateTime, Float, Boolean, create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Specify database config
config = {
    "host": "localhost",
    "port": 3306,
    "user": "charbel",
    "password": "pass123",
    "database": "landon"
}

db_user = config.get("user")
db_pwd = config.get("password")
db_host = config.get("host")
db_port = config.get("port")
db_name = config.get("database")

# Specify connection string
connection_str = f"mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connection_str)
Base = declarative_base()


class Purchase(Base):
    """Purchase object."""
    __tablename__ = "purchases"
    __table_args__ = {"schema": "landon"}

    order_id = Column(Integer, primary_key=True)
    property_id = Column(Integer)
    property_city = Column(String(50))
    property_state = Column(String(50))
    product_id = Column(Integer)
    product_category = Column(String(150))
    product_name = Column(String(150))
    quantity = Column(Integer)
    product_price = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return f"""
            <Purchase(order_id='{self.order_id}', property_id='{self.property_id}',
            property_city='{self.property_city}', property_state='{self.property_state}',
            product_id='{self.product_id}', product_category='{self.product_category}',
            product_name='{self.product_name}', quantity='{self.quantity}'
            product_price='{self.product_price}', order_total='{self.order_total}')>
        """


Base.metadata.create_all(engine)

file_name = "landon.csv"

df = pandas.read_csv(file_name)

df.to_sql(con=engine, name=Purchase.__tablename__, if_exists="append", index=False)

# Verify data was written to db
session = sessionmaker()
session.configure(bind=engine)
s = session()

results = s.query(Purchase).limit(10).all()
for r in results:
    print(r)
