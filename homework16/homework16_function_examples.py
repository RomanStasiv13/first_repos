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





