# Go to your implementation of the Phonebook application from module 1 or any other comprehensive code,
# which you have done during the course, and annotate this code with type hints,
# using knowledge from this lesson.

import json

with open('contact_book.json') as file_object:
    contact_book = json.load(file_object)


def contacts() -> None:
    for i in contact_book['contacts']:
        for k, v in i.items():
            print(k, '-', v)
        print('***********')
    menu()


def choose_main() -> int:
    print('\t Please,choose the operation:\n')
    print('1.Contacts')
    print('2.Options')
    choice = int(input('Enter the number of your choice: '))
    return choice


def menu() -> dict:
    choice = choose_main()
    if choice == 1:
        contacts()
    elif choice == 2:
        user_choice()
    with open('contact_book.json') as file_object:
        contact_book = json.load(file_object)
    return contact_book


def rewrite_json() -> None:
    with open('contact_book.json', 'w') as file_object:
        json.dump(contact_book, file_object)


def contact_menu() -> int:
    print('\t Please,choose the operation:\n')
    print('1.Add new entries')
    print('2.Search')
    print('3.Delete a record for a given telephone number')
    print('4.Update a record for a given telephone number')
    print('5.Exit from contacts')

    choice = int(input('Enter the number of your choice: '))
    return choice


def user_choice() -> None:
    choice = contact_menu()
    if choice == 1:
        add_new_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        exit()
    else:
        print('You choose wrong operation,try again')


def operator_menu(operator: str) -> int:
    print('\t Please,choose the operation:\n')
    print(f'1. {operator} by first name')
    print(f'2. {operator} by last name')
    print(f'3. {operator} by full name')
    print(f'4. {operator} by telephone number')
    print(f'5. {operator} by city or state')

    search_type = int(input(f'Enter the number of {operator} type: '))
    return search_type


def search_contact() -> None:
    search_type = operator_menu('Search')
    value = str(input('Enter search value: '))
    for i in contact_book['contacts']:
        index = 1
        try_again = 0
        for k, v in i.items():
            if index == search_type:
                if v.lower() == value.lower():
                    display_one_contact(i)
                    try_again += 1
            index += 1
    menu()


def display_one_contact(contact: dict) -> None:
    for k, v in contact.items():
        print(k.capitalize(), ':', v.upper())
    print('--------------')


def create_new_contact() -> dict:
    name = input('Enter the name: ')
    surname = input('Enter the surname: ')
    full_name = input('Enter the full name of person: ')
    number = input('Enter the telephone number: ')
    state = input('Enter the state: ')
    new_char_dict = {
        'name': name,
        'surname': surname,
        'full name': full_name,
        'number': number,
        'state': state,
    }
    return new_char_dict


def add_new_contact() -> None:
    new_char = create_new_contact()
    contact_book['contacts'].append(dict(new_char))
    rewrite_json()
    print('New contact added')
    menu()


def delete_contact() -> None:
    print('Please enter the number of contact you want to remove: ')
    fullname_list()
    rem_cont = int(input('')) - 1
    display_one_contact(contact_book['contacts'][rem_cont])
    really = input('Do really want to remove this contact? y/n')
    if really == 'y':
        contact_book['contacts'].pop(rem_cont)
        rewrite_json()
    menu()


def fullname_list() -> None:
    index = 1
    for i in contact_book['contacts']:
        for k, v in i.items():
            if k == 'full name':
                print(index, '-', v)
        index += 1


def update_contact() -> None:
    print('Please enter the number of contact you want to update: ')
    fullname_list()
    up_cont = int(input('')) - 1
    display_one_contact(contact_book['contacts'][up_cont])
    really = input('Do really want to update this contact? y/n')
    if really == 'y':
        value_update(up_cont)
    menu()


def value_update(up_cont: int) -> None:
    update_type = operator_menu('Update')
    value = str(input('Enter update value: '))
    index = 1
    for k, v in contact_book['contacts'][up_cont].items():
        if index == update_type:
            contact_book['contacts'][up_cont][k] = value
            rewrite_json()
            print('Contact updated')

        index += 1


def exit() -> None:
    menu()


if __name__ == '__main__':
    c = menu()

