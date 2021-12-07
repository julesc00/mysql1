import sqlalchemy as db
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3, depth=4, sort_dicts=True)

# Specify database config
config = {
    "host": "localhost",
    "port": 3306,
    "user": "charbel",
    "password": "pass123",
    "database": "projects"
}

db_user = config.get("user")
db_pwd = config.get("password")
db_host = config.get("host")
db_port = config.get("port")
db_name = config.get("database")

# Specify connection string
connection_str = f"mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"

# Connect to db
engine = db.create_engine(connection_str)
connection = engine.connect()

# Pull table metadata
metadata = db.MetaData(bind=engine)
metadata.create_all(engine)

projects = db.Table("projects", metadata, autoload=True, autoload_with=engine)

query = db.select([projects])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

query_by_title = db.select([projects.columns.title])
result_proxy2 = connection.execute(query_by_title)
result_set2 = result_proxy2.fetchall()

pp.pprint(result_set)
for title in result_set2:
    print(title)

