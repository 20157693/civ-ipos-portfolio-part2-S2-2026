from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.task import Base, Task

# This establishes the link to the SQLite database. Use SQLite and save it to tasks.db
engine = create_engine("sqlite:///tasks.db")

# Check if no database exists and if so, creates it.
Base.metadata.create_all(engine)

# Session is a factory (session maker): call Session() to get a new workspace on the DB.
Session = sessionmaker(bind=engine)

def load_tasks():
    """Return every task from the database as a list."""
    session = Session() # connect to db
    tasks = session.query(Task).all() # grab all tasks in list
    session.expunge_all()   # detach objects so they're usable after close
    session.close()
    return tasks

def save_tasks(tasks):
    """Replace all stored tasks with the given list (simple full rewrite)."""
    session = Session()
    session.query(Task).delete()    # clear the currently existing table
    for task in tasks:
        session.add(Task(task.title, task.description,
                         task.due_date, task.status))
    session.commit()
    session.close()