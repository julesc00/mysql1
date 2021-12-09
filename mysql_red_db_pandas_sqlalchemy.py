"""Loading csv data using pandas module, Challenge"""
import pandas
from sqlalchemy import (Column, DateTime, Float, Integer, Boolean, String, create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Specify database config
config = {
    "host": "localhost",
    "port": 3306,
    "user": "charbel",
    "password": "pass123",
    "database": "red"
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


class Order(Base):
    """Create the order object."""
    __tablename__ = "orders"
    __table_args__ = {"schema": "red"}

    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(50))
    cust_name = Column(String(150))
    cust_state = Column(String(150))
    prod_category = Column(String(150))
    prod_number = Column(String(50))
    prod_name = Column(String(150))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return f"""
            <Order(order_num='{self.order_num}', order_type='{self.order_type}',
            cust_name='{self.cust_name}', cust_state='{self.cust_state}',
            prod_category='{self.prod_category}', prod_number='{self.prod_number}',
            prod_name='{self.prod_name}', quantity='{self.quantity}', price='{self.price}'
            discount='{self.discount}', order_total='{self.order_total}')>
        """


Base.metadata.create_all(engine)

filename = "red30.csv"

df = pandas.read_csv(filename)
df.to_sql(con=engine, name=Order.__tablename__, if_exists="append", index=False)

# Verify data was written to db
session = sessionmaker()
session.configure(bind=engine)
s = session()

results = s.query(Order).limit(15).all()
for r in results:
    print(r)
