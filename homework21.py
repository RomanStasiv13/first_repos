### task 1

def to_power(x: int, exp: int):
    if exp == 1:
        return x
    if exp == 0:
        return 1
    if exp < 0:
        raise ValueError
    return x * to_power(x, exp - 1)


print(to_power(3.5, 2))
print(to_power(2, 3))


### task 2

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if index == len(looking_str) // 2:
        return True
    if looking_str[index] != looking_str[-1 - index]:
        return False
    return is_palindrome(looking_str, index + 1)


print(is_palindrome('mom'))
print(is_palindrome('sassas'))
print(is_palindrome('o'))


### task 3

def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError
    if n == 1:
        return a
    if n == 0:
        return 0
    return a + mult(a, n - 1)

print(mult(2,4))
print(mult(2,0))
#print(mult(2, -4))

### task 4

def reverse(input_str: str) -> str:
    if input_str == '':
        return input_str
    return reverse(input_str[1:]) + input_str[0]

print(reverse('hello'))
print(reverse('o'))

### task 5

def sum_of_digits(digit_string: str) -> int:
    if not type(digit_string) is str:
        raise TypeError
    if not digit_string.isalnum():
        raise ValueError
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + int(sum_of_digits(digit_string[1:]))

print(sum_of_digits('26'))
#print(sum_of_digits('test'))
