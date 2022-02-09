# Task 1
# Implement binary search using recursion.

def binary_search(array: list[int], lower: int, higher: int, value: int):
    if higher >= lower:
        middle = (higher + lower) // 2
        if array[middle] == value:
            return True
        elif array[middle] < value:
            return binary_search(array, middle + 1, higher, value)
        return binary_search(array, lower, middle - 1, value)
    return False


array_1 = [i for i in range(1, 100)]
assert binary_search(array_1, 0, len(array_1) - 1, 13) == True
assert binary_search(array_1, 0, len(array_1) - 1, 131) == False
assert binary_search(array_1, 0, len(array_1), 65) == True


# Task 2
# Read about the Fibonacci search and implement it using python. Explore its complexity
# and compare it to sequential, binary searches.
def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_search(arr, value):
    m = 0
    while fibonacci(m) < len(arr):
        m += 1
    index_offset = -1
    while fibonacci(m) > 1:
        index = min(index_offset + fibonacci(m - 2), len(arr) - 1)
        if value > arr[index]:
            m -= 1
            index_offset = index
        elif value < arr[index]:
            m -= 2
        else:
            return index
    if fibonacci(m - 1) and arr[index_offset + 1] == value:
        return index_offset + 1
    return -1

arr = [10,15,17,22,33,40,56]
value = 33
m = fibonacci_search(arr,56)
print(m)