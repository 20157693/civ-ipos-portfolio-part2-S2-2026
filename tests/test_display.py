# test with
# python -m unittest discover -s tests -v
# python -m flake8 ./src
import unittest

from src.task_manager import format_tasks
from src.task import Task


class TestListTasksDisplay(unittest.TestCase):
    """Verify task display is rendered as a formatted table (tabulate)."""

    def test_format_tasks_renders_table(self):
        tasks = [Task("Buy milk", "2 litres", "01-12-2026", "pending")]
        output = format_tasks(tasks)
        self.assertIn("Title", output)   # header row from tabulate
        self.assertIn("+", output)       # grid borders


if __name__ == "__main__":
    unittest.main()
