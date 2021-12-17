# # Task 1
# # Method overloading.
# # Create a base class named Animal with a method called talk and then create two subclasses:
# # Dog and Cat, and make their own implementation of the method talk be different. For instance,
# # Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# # Also, create a simple generic function,
# # which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.


def input_animal():
    animal = input('Dog or Cat: ').lower()
    name = input('Enter the name of your pet: ')
    if animal == 'cat':
        pet = Cat(name)
    if animal == 'dog':
        pet = Dog(name)
    print(pet.talk())


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        return f'{self.name} says "meow"'

class Dog(Animal):
    def talk(self):
        return f'{self.name} says "woof woof"'


if __name__ == '__main__':
     p = input_animal()


# Task2
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class
# and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
import json


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: str):
        book = Book(name, year, author)
        for lib_author in self.authors:
            if lib_author['name'] == author:
                self.books.append(json.loads(str(book)))
                lib_author['books'].append(name)
                Book.book_amount += 1
                return book

    def add_author(self, name: str, country: str, birthday: str):
        author = Author(name, country, birthday)
        self.authors.append(json.loads(str(author)))
        return author

    def display_book_amount(self):
        return Book.book_amount

    def group_by_year(self, year: int):
        year_editions = []
        for book in self.books:
            if book['year'] == year:
                year_editions.append(book['name'])
        return year_editions

    def group_by_author(self, author: 'Author'):
        author_editions = None
        for aut in self.authors:
            if aut['name'] == author:
                author_editions = (aut['books'])
        return author_editions


class Book():
    book_amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        book_dict = {
            'name': self.name,
            'year': self.year,
            'author': self.author
        }
        books = json.dumps(book_dict)
        return books

    def __repr__(self):
        return self.__str__()


class Author():
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        author_info = {
            'name': self.name,
            'country': self.country,
            'birthday': self.birthday,
            'books': self.books
        }
        author = json.dumps(author_info)
        return author

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    l = Library('Libr')
    l.add_author("Taras Shevchenko", "Ukraine", "09.03.1814")
    l.add_author("William Shakespeare", "England", "26.04.1564")
    l.add_author("Edgar Allan Poe", "USA", "19.01.1809")
    l.add_author("Stephen King", "USA", "21.09.1947")
    l.new_book("Kobzar", 1840, "Taras Shevchenko")
    l.new_book("Carrie", 1974, "Stephen King")
    l.new_book("It ", 1986, "Stephen King")
    l.new_book("Misery", 1987, "Stephen King")
    l.new_book("The Eyes of the Dragon", 1987, "Stephen King")
    l.new_book("The Tommyknockers", 1987, "Stephen King")
    l.new_book("The Raven", 1845, "Edgar Allan Poe")
    l.new_book("The Tell-Tale Heart", 1843, "Edgar Allan Poe")
    l.new_book("Annabel Lee", 1849, "Edgar Allan Poe")
    l.new_book("Othello", 1605, "William Shakespeare")
    l.new_book("Macbeth", 1606, "William Shakespeare")

    print(l.group_by_year(1987))
    print(l.group_by_author("Edgar Allan Poe"))
    print(l.display_book_amount())

# Task 3
# Fraction
# Create a Fraction class, which will represent all basic arithmetic logic for fractions
# (+, -, /, *) with appropriate checking and error handling.

