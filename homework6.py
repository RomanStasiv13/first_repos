# Task 1
# A simple function.
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.
def favorite_movie(name):
    print(f'My favorite movie is named {name}')
if __name__ == '__main__':
    user_movie=favorite_movie(input('What is your fav movie?'))

# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(country_name,capital):
    return dict(zip(country_name.split(), capital.split()))


if __name__ == '__main__':
    capital_dict = make_country(input('Enter the country ').lower().capitalize(), input('Enter the capital ').lower().capitalize())
    print(capital_dict)


# Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter

def make_operation(operator,*args):
    operator=input('''please choose the operation you would like to complete:
    + for addition
    - for substraction
    * for multiplication
    ''')
    args=input('Enter the arguments divided by a space').split()
    count=0
    calc=0
    for num in args:
        count+=1
        question=str(num.strip())
        if operator!='+' or operator!='-' or operator!='*'
            print('Enter valid operator: + or - or *')
        if question[0]=='-':
            question=question[1:]
        if not question.isdigit():
                print('Invalid operation:arguments must be numbers')
                break
        if count==1:
            calc=int(num)
        if operator=='+' and count>1:
            calc+=int(num)
        elif operator=='-' and count>1:
            calc-=int(num)
        elif operator=='*'and count>1 :
            calc*=int(num)

        print(calc)
if __name__ == '__main__':

    calculator = make_operation(input('Press enter'))

# Напишите функцию которая будет переводить возраст с Земного на Марсианский. В году на Земле 365 дней а на марсе 687

def mars_age(age=0):
    mars=round(age*365/687)
    return mars
assert mars_age(10)==5
assert mars_age(63)==33
assert mars_age(1000)==531

# Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
# Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"

def greet(name='-',word='-'):
    return f'{str(name).capitalize()} ты сегодня {str(word)}!'

assert greet("111", "2") == "111 ты сегодня 2!"
assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
assert greet("николай") == "Николай ты сегодня -!"

# Напишите функцию joinA которая принимает неограниченное количество значений любого типа
# и возвращает строку где эти значения склеены через символ A
# Попробуйте написать с помощью компрехеншена одной строкой return ___magic___

def joinA(*args):

     ___magic___ = "A".join([str(i) for i in args])
     return ___magic___

assert joinA("Привет", "мир", "!") == "ПриветAмирA!"
assert joinA("Привет", 1, 2, 3, True) == "ПриветA1A2A3ATrue"
assert joinA() == ""


# Допишите игру 21.
# Правила просты генерим колоду с "картами" и пока челвоек не скажет "no" даем ему карту.
# Потом "сдаем" себе до набора 15ти если набрал 15ть или больше сравниваем.
# Если у человека перебор - сразу ему поражение.









