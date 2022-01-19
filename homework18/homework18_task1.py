# Task 1
# File Context Manager class
# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
from datetime import  datetime
from typing import IO

class FileContextManager:
    open_counter: int = 0

    @classmethod
    def get_num_of_opens(cls):
        return cls.open_counter

    def __init__(self, file_name: str, mode: str = 'r'):
        self.__file_name = file_name
        self.__mode = mode
        self.__file = open(file_name, mode)
        self.__logger = open('logger.txt', 'a')

    def __enter__(self) -> IO:
        self.__logger.write(f'Opened: {self.__file_name} with mode: {self.__mode} at {datetime.now().time()}.\n')
        FileContextManager.open_counter += 1
        return self.__file

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None):
        self.__logger.write(f'Closed: {self.__file_name} at {datetime.now().time()} (File was opened {FileContextManager.open_counter} times).\n')
        self.__logger.close()
        self.__file.close()
        return None



if __name__ == '__main__':
    with FileContextManager('hw_18_file.txt', 'w') as file:
        file.write('To hell with good intentions')

