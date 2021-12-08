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
