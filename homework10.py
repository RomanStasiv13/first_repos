# Task 1
# School
# Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, name='', age='', sex='male'):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(Person):
    def teacher_atr(self, salary='', grade='', seniority=''):
        self.salary = salary
        self.grade = grade
        self.seniority = seniority

    def teacher_info(self):
        return f'Name:{self.name},\nAge:{self.age},\nSex:{self.sex},\nSalary:{self.salary},\nGrade:{self.grade},\nYears of work:{self.seniority}'


class Student(Person):
    def student_atr(self, course='', score='', ed_form='scholarship'):
        self.course = course
        self.score = score
        self.ed_form = ed_form

    def student_info(self):
        return f'Name:{self.name},\nAge:{self.age},\nSex:{self.sex},\nCourse:{self.course},\nAverage score:{self.score},\nEducation form:{self.ed_form}'


if __name__ == '__main__':
    p1 = Teacher('Mr.Smith', '49', 'male')
    p1.teacher_atr('9000$', 'prof.', '23')
    print(p1.teacher_info())
    p2 = Student('Jenny', '19', 'female')
    p2.student_atr('C#', '89', 'distance')
    print(p2.student_info())


# Task 2
# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists

class Mathematician:
    def square_nums(self, *args):
        return [x * x for x in args]

    def remove_positives(self, *args):
        return [x for x in args if x < 0]

    def filter_leaps(self, *args):
        return [x for x in args if x % 400 == 0 or x % 4 == 0 and not x % 100 == 0]


# Task 3
# Product Store


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductInStore:
    def __init__(self, storage):
        self.storage = storage
        self.amount = 0
        self.price = storage.price
        self.discount = 0
        self.count = 0


class ProductStore:
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        some_product = ProductInStore(product)
        some_product.amount = amount
        some_product.count = amount

        self.products.append(some_product)
        print(f'Product {product.name} was added to store.')

    def set_discount(self, identifier, percent):
        for product in self.products:
            if identifier == product.storage.name:
                product.discount = percent
                product.price = product.price - (product.price * percent / 100)
                print(f'{percent}% discount was set')

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.storage.name == product_name:
                if product.amount >= amount:
                    product.amount -= amount
                    print(f'Product {product.storage.name} was sold')
                elif product.amount > 0 and amount > product.amount:
                    delta = amount - product.amount
                    product.amount = 0
                    print(
                        f'You have bought all our {product.storage.name}.You can buy {delta} {product.storage.name} somewhere else ')
                else:
                    print('This item was sold out')

    def get_income(self):
        income = 0
        for product in self.products:
            income += (product.count - product.amount) * product.price
        print(f'The store was earn {income}$')

    def get_all_products(self):
        store_items = []
        for product in self.products:
            if product.amount != 0:
                store_items.append(
                    {
                        'type': product.storage.type,
                        'name': product.storage.name,
                        'amount': product.amount,
                        'price': product.storage.price,
                        'discount': product.discount,
                        'price with discount': product.price

                    }
                )
        print(f'Available items:\n{store_items}')

    def get_product_info(self, product_name):
        for product in self.products:
            if product.storage.name == product_name:
                return product.storage.name, product.amount


if __name__ == '__main__':
    p = Product('Food', 'Ramen', 1.5)
    p1 = Product('Sport', 'Ball', 100)
    s = ProductStore()
    s2 = ProductStore()
    s.add(p, 10)
    s.add(p1, 7)
    s2.add(p, 70)
    s2.add(p1, 15)
    s.set_discount('Ramen', 20)
    s2.set_discount('Ramen', 10)
    s.set_discount('Ball', 12)
    s2.set_discount('Ball', 35)
    s.sell_product('Ramen', 2)
    s.sell_product('Ball', 3)
    s2.sell_product('Ball', 10)
    s2.sell_product('Ramen', 40)
    s.sell_product('Ball', 2)
    s.get_all_products()
    s2.get_all_products()
    s.get_income()
    s2.get_income()
