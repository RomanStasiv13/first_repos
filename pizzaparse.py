from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class PizzaPrice:
    price: int
    weight: int

    def __repr__(self):
        return f'Цена: {self.price} | Вес: {self.weight}'

    def to_json(self):
        return {'price': self.price,
                'weight': self.weight}


@dataclass
class Pizza:
    name: str
    descr: str
    img: str
    variants: list[PizzaPrice]

    def to_json(self):
        return {'name': self.name,
                'variants': [i.to_json() for i in self.variants]}

    def __repr__(self):
        return f'''
        Название: {self.name}
        {self.img}
        Описание: {self.descr}
        Размер: {self.variants}
        '''


class PizzasList:
    BASE_URL = 'https://cipollino.ua/pizza'

    def __iter__(self):
        session = requests.Session()
        self.pizza_list = []
        res = session.get(self.BASE_URL, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
        })
        bs = BeautifulSoup(res.text, 'lxml')
        main_div_list = bs.find_all('div', class_='cipollino-product-item')
        for one_block in main_div_list:
            name = one_block.find('div', class_='cipollino-product-name').text.strip()
            description = one_block.find('div', class_='cipollino-product-ingredients').text.strip()
            image = one_block.find('img').attrs['data-src']
            options_list = one_block.find_all('div', class_='cipollino-product-option')
            pizzas_vars = []
            for variant in options_list:
                price = variant.find('div', class_='cipollino-product-option-price').find('p',
                                                                                          class_='cipollino-price').text
                weight = variant.find('div', class_='cipollino-product-option-price').find('p',
                                                                                           class_='cipollino-weight').text
                pizzas_vars.append(PizzaPrice(price, weight))
            pizza = Pizza(name, description, image, pizzas_vars)
            self.pizza_list.append(pizza)
        return self

    def __next__(self) -> Pizza:
        if self.pizza_list:
            return self.pizza_list.pop()
        raise StopIteration


if __name__ == '__main__':
    for p in PizzasList():
        #print(p.to_json())
        print(p)
