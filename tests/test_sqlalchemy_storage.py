# Test with:
# python -m unittest discover -s tests -v
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# This part should fail until Base has been implemented.
from src.task import Base, Task

class TestSQLAlchemyStorage(unittest.TestCase):
    def setUp(self):
        # Create a dummy database in memory and test in it.
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def test_task_is_saved_to_database(self):
        # Add a task and save it.
        self.session.add(Task("Buy milk", "2 litres", "01-12-2026"))
        self.session.commit()

        # Test if entry correctly added
        result = self.session.query(Task).all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Buy milk")