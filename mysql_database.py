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


def add_new_project(cursor, project_title, project_description,
                    task_descriptions):
    """Encapsulate add items to db operation"""

    project_data = (project_title, project_description)

    cursor.execute("""INSERT INTO projects(title, description)
        VALUES (%s, %s)""", project_data)

    project_id = cursor.lastrowid
    tasks_data = []

    for description in task_descriptions:
        task_data = (project_id, description)
        tasks_data.append(task_data)

    cursor.executemany("""INSERT INTO tasks(project_id, description)
    VALUES (%s, %s)""", tasks_data)


if __name__ == "__main__":
    db = connect("projects")

    cursor = db.cursor()

    tasks = ["Practice algorithms", "Practice Oracle SQL", "Practice challenges"]
    add_new_project(cursor, "Learn advanced Go", "Learn Golang for the web", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    pp.pprint(project_records)

    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    pp.pprint(tasks_records)

    db.close()
