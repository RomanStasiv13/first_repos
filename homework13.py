# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
from functools import wraps


def logger(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        print(func.__name__)
        return res
    return wrapper


    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg**2 for arg in args]



f1 = add(4,5)
print(f1)
f2 = square_all(5,6,7,8)
print(f2)


# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def func_slogan(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            func_str = func(*args,*kwargs)
            for word in words:
                func_str = func_str.replace(word, "*")
            return func_str
        return wrapper
    return func_slogan



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"



# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.


def arg_rules(type_: type, max_length: int, contains: list):
    def func_slogan(func):
        @wraps(func)
        def wrapper(name):
            f = func(name)
            if len(name) > max_length:
                print('Error: Slogan is too long')
                return False
            if type(name) != type_:
                print("Error: Wrong type!")
                return False
            for contain in contains:
                if name.find(contain) == -1:
                    print(f"Error: Name should contain: {contains} ")
                    return False
            return f
        return wrapper
    return func_slogan




@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'