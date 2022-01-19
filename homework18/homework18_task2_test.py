# Task 2
# Writing tests for context manager
# Take your implementation of the context manager class from Task 1 and write tests for it.
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
# And also, write tests when your class raises errors or you have errors in the runtime context suite.

import unittest
from homework18_task1 import FileContextManager


class Test(unittest.TestCase):
    def test_file_opened(self):
        with FileContextManager('hw_18_file.txt', 'w') as file:
            self.assertFalse(file.closed)
            file.close()

    def test_counter(self):
        with FileContextManager('hw_18_file.txt', 'w') as file:
            file.close()
        with FileContextManager('hw_18_file.txt', 'w') as file:
            file.close()
        self.assertEqual(FileContextManager.open_counter, 2)

    def test_logger(self):
        with FileContextManager('logger.txt') as logger:
            self.assertIn('Opened', logger.readlines()[0])
        with FileContextManager('logger.txt') as logger:
            self.assertIn('Closed', logger.readlines()[-1])



if __name__ == '__main__':
    unittest.main
