import csv
import mysql.connector as mysql
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3, sort_dicts=True, depth=4)

connection = mysql.connect(
    user="root",
    password="pass123",
    host="localhost",
    database="sales",
    allow_local_infile=True  # For SQL loading
)

cursor = connection.cursor()

create_query = """CREATE TABLE salesperson(
    id INT(255) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
)"""

cursor.execute("DROP TABLE IF EXISTS salesperson")

cursor.execute(create_query)

# with open("salespeople.csv", "r") as f:
#     csv_data = csv.reader(f)
#     for row in csv_data:
#         row_tuple = tuple(row)
#         cursor.execute("""
#         INSERT INTO salesperson(
#             first_name,
#             last_name,
#             email_address,
#             city,
#             state)
#         VALUES ("%s", "%s", "%s", "%s", "%s")
#         """, row_tuple)

# Load csv with SQL
q = """LOAD DATA INFILE '/Users/julio_briones/Documents/Dev/Python/Core/mysql1/salespeople.csv' INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"' (first_name, last_name, email_address, city, state);"""

cursor.execute(q)

connection.commit()

cursor.execute("SELECT * FROM salesperson LIMIT 10")
pp.pprint(cursor.fetchall())

connection.close()
