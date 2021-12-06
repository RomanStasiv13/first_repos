# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?
def oops():
    raise IndexError

def catch_oops():
    try:
        err=oops()
    except IndexError:
        print('oops:(')

if __name__ == '__main__':
    first_error = catch_oops()

# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def sqroot():
    try:
        a = int(input('input a'))
        b = int(input('input b'))
        rez = a ** 2 / b
        print(rez)

    except ValueError:
        print('MUST BE NUMBERS!')
        raise
    except ZeroDivisionError:
        print('b CANNOT BE ZERO!')
        raise


if __name__ == '__main__':
    count_err = sqroot()