import os


class Operation: # Клас для роботи з файлом (Базовий Клас)
    def __init__(self): # Метод конструктор, який оголошуэ змінні
        self.path = None
        self.directory = '\\'
        self.file_name = None
        self.value = None
        self.content = None

    def get_file(self): # Метод, який приймає файл від користувача
        self.path = input('Введіть шлях до файла.')
        with open(os.path.join(os.path.dirname(__file__), self.path), 'r', encoding="utf-8") as input_file:
            self.content = input_file.read()
        input_file.close()

    def get_path(self): # Метод для отримання шляху до файлу та назви результуючого файлу
        dir_list = self.path.split('\\')
        i = 0
        directory = ''
        while i <= len(dir_list) - 2:
            directory += dir_list[i] + '\\'
            i += 1
        self.directory = directory
        self.file_name = 'result_' + (dir_list[len(dir_list) - 1].split('.'))[0] + '.txt'

    def create_result_file(self): # Метод для сворення результуючого файлу
        self.get_path()
        with open(f'{self.directory + self.file_name}', 'w+') as res_file:
            res_file.write('\n\n\n\n\n')

    def rewrite_line(self, index, text): # Метод для перезаписування строк у результуючому файлі построково
        a_file = open(f'{self.directory + self.file_name}', "r")
        list_of_lines = a_file.readlines()
        list_of_lines[index] = text

        a_file = open(f'{self.directory + self.file_name}', "w")
        a_file.writelines(list_of_lines)
        a_file.close()


class Counter(Operation): # Клас для підрахування кількості символів
    def __init__(self): # Метод конструктор класу який приймає у змінні символи для підрахування
        super(Counter, self).__init__()
        self.vowels = 'аеєиіїоуюя'
        self.consonants = 'бвгґджзйклмнпрстфхчшщь'
        self.integers = '1234567890'
        self.punctuation = '.,!?"\'-;:'

    def vowel_counter(self): # Метод для підрахування голосних літер
        v_counter = 0
        for char in self.content:
            if char.lower() in self.vowels:
                v_counter += 1
        self.rewrite_line(0, f'У файлі {v_counter} голосних літер\n')
        print(f'У файлі {v_counter} голосних літер')

    def consonants_counter(self): # Метод для підрахування приголосних літер
        c_counter = 0
        for char in self.content:
            if char.lower() in self.consonants:
                c_counter += 1
        self.rewrite_line(1, f'У файлі {c_counter} приголосних літер\n')
        print(f'У файлі {c_counter} приголосних літер')

    def integer_counter(self): # Метод для підрахування цифер
        i_counter = 0
        for char in self.content:
            if char in self.integers:
                i_counter += 1
        self.rewrite_line(2, f'У файлі {i_counter} цифер\n')
        print(f'У файлі {i_counter} цифер')

    def punctuation_counter(self): # Метод для підрахування знаків пунктуації
        p_counter = 0
        for char in self.content:
            if char in self.punctuation:
                p_counter += 1
        self.rewrite_line(3, f'У файлі {p_counter} розділових знаки(-ів)\n')
        print(f'У файлі {p_counter} розділових знаки(-ів)')

    def space_counter(self): # Метод для підрахування пробілів
        s_counter = 0
        for char in self.content:
            if char == ' ':
                s_counter += 1
        self.rewrite_line(4, f'У файлі {s_counter} пробілів\n')
        print(f'У файлі {s_counter} пробілів')


class UserInterface: # Клас інтерфейс
    choice_1 = None
    choice_2 = None

    def menu(self): # Метод меню
        print('\t РОБОТА З ФАЙЛАМИ \n')
        print('1.Почати роботу')
        print('2.Вихід')
        self.choice_1 = int(input('Введіть номер пункту: '))

    def operation_menu(self): # Метод меню операцій для підрахунку символів
        print('\t Операції над файлом \n')
        print('1.Підрахувати кількість голосних літер')
        print('2.Підрахувати кількість приголосних літер')
        print('3.Підрахувати кількість цифер')
        print('4.Підрахувати кількість знаків пунктуації')
        print('5.Підрахувати кількість пробілів')
        self.choice_2 = (input('Введіть номер або номери пунктів через кому: ')).split(',')

    def menu_choice(self): # Метод логіка меню
        self.menu()
        c = Counter()
        if self.choice_1 == 1:
            c.get_file()
            self.operation_menu()
            c.create_result_file()
            for i in self.choice_2:
                if i == '1':
                    c.vowel_counter()
                elif i == '2':
                    c.consonants_counter()
                elif i == '3':
                    c.integer_counter()
                elif i == '4':
                    c.punctuation_counter()
                elif i == '5':
                    c.space_counter()
                else:
                    exit()
        else:
            exit()




if __name__ == '__main__':
    m = UserInterface()
    m.menu_choice()