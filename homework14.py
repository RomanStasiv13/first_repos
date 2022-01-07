import re


# Task 1
# Create a class method named `validate`, which should be called from the `__init__` method
# to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.


class Email:
    email = ''

    def __init__(self, email):
        self.email = email
        self.validate(self.email)

    @classmethod
    def validate(cls, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            print("Valid Email")
            cls.email = email
        else:
            print("Invalid Email")

    @property
    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__


if __name__ == '__main__':
    a = Email("4567")
    b = Email('safdfasdgf@gmail.com')


# Task 2

# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!
# You can refactor the existing code.

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def to_employ(self):
        return f'My workers {self.workers}'

    @to_employ.setter
    def to_employ(self, worker: "Worker"):
        if isinstance(worker, Worker) and worker not in self.workers:
            if worker.boss == None and worker.company == None:
                self.workers.append(worker)
                worker.hired(self)
        return self.workers


class Worker:

    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name
        self.company = None
        self.boss = None

    def hired(self, boss: "Boss"):
        if isinstance(boss, Boss):
            self.boss = boss.name
            self.company = boss.company

    def __str__(self):
        return f'ID: {self.id} Name:{self.name}'

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    b1 = Boss(13131, 'Jack', 'Apple')
    b2 = Boss(66666, 'Corey', 'Lego')
    w1 = Worker(22313, 'Eugene')
    w2 = Worker(33242, 'Robert')
    w3 = Worker(23232, 'May')
    b1.to_employ = w1
    b1.to_employ = w2
    b2.to_employ = w1
    b2.to_employ = w3
    print(b1.to_employ)
    print(b2.to_employ)
    print(w1.boss,w1.company)
    print(w2.boss,w2.company)
    print(w3.boss,w3.company)


# Task 3
# Write a class TypeDecorators which has several methods for converting results of functions to a specified type
# (if it's possible)

from functools import wraps


def type_decorators(needed_type: type):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            try:
                return needed_type(val)
            except ValueError:
                return 'Wrong type!!!'

        return wrapper

    return deco


@type_decorators(int)
def to_int(val: str):
    return val
@type_decorators(str)
def to_str(val: str):
    return val
@type_decorators(bool)
def to_bool(val: str):
    return val
@type_decorators(float)
def to_float(val: str):
    return val



if __name__ == '__main__':
    fl = to_float(6)
    print(fl, type(fl))
    bl = to_bool(6 > 9)
    print(bl, type(bl))
    st = to_str(8 < 6)
    st1 = to_str(6)
    print(st, type(st))
    print(st1, type(st1))
    num = to_int('6')
    num1 = to_int('ad')
    print(num, type(num))
    print(num1, type(num1))
