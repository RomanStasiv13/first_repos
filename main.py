###lsn01

###задание 1.0 В курсе 44 занятия с домашними работами. Для получения диплома надо сдать 80%.
###Сколько заданий нужно будет сдеать? Ответ выведите с помощью функции print()

total = 44
rez = int(total * 0.8)
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez ==35

###задание Есть координаты (переменные) x1, y1 и x2, y2 рассчитайте и выведите расстояние между точками.

x1=5
x2=-6
y1=4
y2=0
import math
print("lenth :",math.fabs(((x1-x2)**2 + (y1-y2)**2)**0.5))

###задание Создайте переменные Высоты ширины и глубины для прямоугольника и
###выведите с помощью команды print площадь диагонального сеения.
###(представьте себе что нужно рассчитать площадь щифера для крыши.) Стоимость "листа" шифера - 600грн. Размеры 3х4м.
###Сколько листов вам понадобиться купить? Выведете на экран количество, сумму, остаток шифера.

heigh = 10
width = 20
depth = 5
diagonal_area = (((width)**2 + (depth)**2)**0.5)*heigh
print(diagonal_area)

slate_price = 600
slate_plate_area = 3*4
roof_area = diagonal_area
print(f'Площа даху{roof_area}')

import math
number_of_plates = math. ceil(roof_area/slate_plate_area)
print(f'Кількість листів: {number_of_plates}')

total_sum = number_of_plates * slate_price
print(f'Загальна сума: {total_sum}')

remainder_of_plates = roof_area % slate_plate_area
print(f'Остаток: {remainder_of_plates}')


###Отредактируйте код чтобы выполнялись ассерт инструкции. (потребуется знание строковых функций.)

var1 = 'pyThoN'
var1 = var1.lower().capitalize()
print(var1)
assert var1 == 'Python'

var1 = var1.upper()
print(var1)
assert var1 == 'PYTHON'

var1 = var1.lower()
print(var1)
assert var1 == 'python'

var1 = " python "
var1 = var1.strip()
print(var1)
assert var1 == 'python'

###Сделайте чтобы он выводил 'Привіт Остап' еще тремя способами форматирования.
###И да они все вам понадобятся. f-строки, .format и форматирование через "%"

name = "Остап"
print("Привет "+name)
print("Привет {}".format(name))
print(f'Привет {name}')
print('Привет %s' %name)

###Задача Почините код

price = 12
weight = 3.4121
rez = 0
rez = f'Итого: {round(price*weight,2)}'
print(rez)
assert rez == 'Итого: 40.95'

###Задача Используя форматирование и черную магию заставьте этот код выполниться без ошибок.
###Строки с обьявлением переменных и assert не трогаем!
###Подсказка: 54 в битовом представлении - 110110

number = 12
username = "ираклий"
access_mask = 54
hour_price=15.321
rez = 0
rez =(f'{str(number).zfill(6)} {username.capitalize()} {bin(access_mask)[2:]} {round(hour_price,2)}')
print(rez)
assert  rez == '000012 Ираклий 110110 15.32'

###Задача Используя слайсы, конкатенацию (обьединение) и смекалку заставьте код работать
base_str = 'Корова'
rez = 0
rez = base_str[4].upper()+base_str[1:4]+base_str[4].replace('в','н')+base_str[-1]
print(rez)
assert rez == 'Ворона'

###Задача Поменяйте местами значения в переменных

a = 10
b = 55

c = a
a = b
b = c
print(a)
print(b)

assert a==55 and b==10, "Не поменялось. :("




