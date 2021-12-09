from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Specify database config
config = {
    "host": "localhost",
    "port": 3306,
    "user": "charbel",
    "password": "pass123",
    "database": "household"
}

db_user = config.get("user")
db_pwd = config.get("password")
db_host = config.get("host")
db_port = config.get("port")
db_name = config.get("database")

# Specify connection string
connection_str = f"mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connection_str, echo=True)

Base = declarative_base()


# Create db objects (tables) using the ORM.
class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {"schema": "household"}

    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return f"<Project(title'{self.title}', description='{self.description})'>"


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"schema": "household"}

    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("household.projects.project_id"))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return f"<Task(description='{self.description}')>"


Base.metadata.create_all(engine)

# create a new session to be able to query/transact
session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

# Enter new entries
organize_closet_project = Project(title="Organize closet", description="Try to get things organized in there.")
session.add(organize_closet_project)
session.commit()  # This saves changes to db, so project_id in the tasks gets initialized.

# Create tasks to associate with a household project.
tasks = [
    Task(project_id=organize_closet_project.project_id, description="Sweep the nasty floor."),
    Task(project_id=organize_closet_project.project_id, description="Mop that swept floor."),
    Task(project_id=organize_closet_project.project_id, description="Order things around.")
]

# Save multiple entries at once.
session.bulk_save_objects(tasks)
session.commit()

# Query entries
projects = session.query(Project).filter_by(title="Organize closet").first()
print(projects)

tasks_query = session.query(Task).all()
print(tasks_query)
