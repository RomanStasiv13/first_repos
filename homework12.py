# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def local_var():
    fst = 'hello'
    sec = 2
    trd = []


print(local_var.__code__.co_nlocals)


# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def function(a):
    def upp(b):
        return a ** b

    return upp


f = function(4)
print(f(5))

# Task 3
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(nums: list, func1, func2):
    if [num for num in nums if num < 0]:
        return func2
    return func1


def square_nums(nums: list):
    return [num ** 2 for num in nums]


def remove_negatives(nums: list):
    return [num for num in nums if num > 0]
