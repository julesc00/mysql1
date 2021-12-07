import mysql.connector as mysql
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3, sort_dicts=True, depth=4)


def connect(db_name):
    try:
        return mysql.connect(
            host="localhost",
            user="charbel",
            port=3306,
            password="pass123",
            database=db_name
        )
    except ConnectionError as e:
        print(e)


if __name__ == "__main__":
    db = connect("projects")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    pp.pprint(project_records)

    db.close()
