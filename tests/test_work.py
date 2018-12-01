from crawler.work import Work
from unittest.mock import Mock
from queue import Empty
import unittest
import uuid
import types

class TestWork(unittest.TestCase):
    def test_it_does_not_add_work_already_done(self):
        name = str(uuid.uuid4())
        work = Work()
        work.put(name)
        work.get(timeout=0.1)
        work.put(name)

        self.assertRaises(Empty, lambda: work.get(timeout=0.1))
