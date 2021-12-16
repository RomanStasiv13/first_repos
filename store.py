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
                    print(f'You have bought all our {product.storage.name}.You can buy {delta} {product.storage.name} somewhere else ')
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
    s.add(p, 10)
    s.add(p1, 2)
    s.set_discount('Ramen', 20)
    s.set_discount('Ball', 12)
    s.sell_product('Ramen', 2)
    s.sell_product('Ball', 3)
    s.sell_product('Ball',2)
    s.get_all_products()
    s.get_income()
