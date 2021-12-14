# Task 1
# A Person class
# Make a class called Person. Make the __init__() method take firstname, lastname,
# and age as parameters and add them as attributes. Make another method called talk() which makes prints a greeting
# from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname},{self.lastname} and I'm {self.age} years old")


if __name__ == '__main__':
    character = Person('Carl', 'Johnson', '26')
    character.talk()


# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dogage):
        self.dogage = dogage

    def human_age(self):
        return self.age_factor * self.dogage


# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python.


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channel_names):
        self.channel_names = channel_names
        self.ch_index = 0

    def first_channel(self):
        self.ch_index = 0
        return self.channel_names[self.ch_index]

    def last_channel(self):
        self.ch_index = len(self.channel_names) - 1
        return self.channel_names[self.ch_index]

    def turn_channel(self, N):
        if N in range(1, len(self.channel_names) + 1):
            self.ch_index = N - 1
            return self.channel_names[self.ch_index]
        else:
            return "There is no such channel!"

    def next_channel(self):
        self.ch_index = (self.ch_index + 1) % len(self.channel_names)
        return self.channel_names[self.ch_index]

    def previous_channel(self):
        self.ch_index = (self.ch_index - 1) % len(self.channel_names)
        return self.channel_names[self.ch_index]

    def current_channel(self):
        return self.channel_names[self.ch_index]

    def is_exist(self, ex_channel):
        if ex_channel in self.channel_names or ex_channel in range(1, len(self.channel_names) + 1):
            return True
        else:
            return False


if __name__ == '__main__':
    controller = TVController(CHANNELS)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(1))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
    print(controller.is_exist(4))
    print(controller.is_exist("BBC"))






### Бонусы ###
# Создайте класс Friend для хранения имени name и телефона phone. Обратите внимание, у друга может не быть телефона.

class Friend:
    def __init__(self, name='', phone=''):
        self.name = name
        self.phone = phone


u1 = Friend("Андрей", "+380331233333")
u2 = Friend("Петр", )

assert hasattr(u1, "name")
assert hasattr(u1, "phone")
assert u1.name == "Андрей"
assert u2.name == "Петр"
assert u1.phone == "+380331233333"
assert u2.phone == ""


# Задача Напишите класс который будет "рисовать" букву псевдографикой.

class SymbolA:
    def __init__(self, symbol='#'):
        self.symbol = symbol

    def picture(self):
        return f' {self.symbol * 3}\n{self.symbol}  {self.symbol}\n{self.symbol * 4}\n{self.symbol}  {self.symbol}'

    def display(self):
        print(self.picture())

    def line(self, n):
        lines = self.picture().split('\n')
        print(lines[n])


if __name__ == '__main__':
    a = SymbolA('@')
    a.line(0)
    a.line(1)
    a.line(2)
    a.line(3)

    a2 = SymbolA('$')
    a2.line(0)
    a2.line(1)
    a2.line(2)
    a2.line(3)



