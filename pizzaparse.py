import requests
from bs4 import BeautifulSoup
import lxml
from dataclasses import dataclass


@dataclass
class PizzaPrice:
    price: int
    weight: int


@dataclass
class Pizza:
    name: str
    descr: str
    img: str
    variants: list[PizzaPrice]


class PizzasList:
    BASE_URL = 'https://cipollino.ua/pizza'

    def __iter__(self):
        session = requests.Session()
        res = session.get(self.BASE_URL, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
        })
        bs = BeautifulSoup(res.text, 'lxml')
        main_div_list = bs.find_all('div', class_='cipollino-product-item')
        pizza_list = []
        for one_block in main_div_list:
            name = one_block.find('div', class_='cipollino-product-name').text.strip()
            description = one_block.find('div', class_='cipollino-product-ingredients').text.strip()
            image = one_block.find('div', class_='cipollino-product-ingredients').text.strip()
            options_list = one_block.find_all('div', class_='cipollino-product-option')
            pizzas_vars = []
            for variant in options_list:
                price = variant.find('div',class_='cipollino-product-option-price').find('p',class_='cipollino-price').text
                weight = variant.find('div',class_='cipollino-product-option-price').find('p',class_='cipollino-weight').text
                pizzas_vars.append(PizzaPrice(price,weight))

            pizza = Pizza(name,description,image,pizzas_vars)
            pizza_list.append(pizza)
        self.pizza_list = pizza_list
        return self

    def __next__(self) -> Pizza:
        if self.pizza_list:
            return self.pizza_list.pop()
        raise StopIteration


if __name__ == '__main__':
    for p in PizzasList():
        print(p)