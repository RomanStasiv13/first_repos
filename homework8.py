# Task 1
# Files
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings;
# add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.

with open('myfile.txt', 'w') as file_object:
    file_object.write('Hello file world!')

with open('myfile.txt', 'r') as file_object:
    print(file_object.read())

# Task 2
# Extend Phonebook application

import json

with open('contact_book.json') as file_object:
    contact_book = json.load(file_object)


def contacts():
    for i in contact_book['contacts']:
        for k, v in i.items():
            print(k, '-', v)
        print('***********')
    menu()


def choose_main():
    print('\t Please,choose the operation:\n')
    print('1.Contacts')
    print('2.Options')
    choice = int(input('Enter the number of your choice: '))
    return choice


def menu():
    choice = choose_main()
    if choice == 1:
        contacts()
    elif choice == 2:
        user_choice()
    with open('contact_book.json') as file_object:
        contact_book = json.load(file_object)
    return contact_book



def rewrite_json():
    with open('contact_book.json', 'w') as file_object:
        json.dump(contact_book, file_object)


def contact_menu():
    print('\t Please,choose the operation:\n')
    print('1.Add new entries')
    print('2.Search')
    print('3.Delete a record for a given telephone number')
    print('4.Update a record for a given telephone number')
    print('5.Exit from contacts')

    choice = int(input('Enter the number of your choice: '))
    return choice


def user_choice():
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


def operator_menu(operator):
    print('\t Please,choose the operation:\n')
    print(f'1. {operator} by first name')
    print(f'2. {operator} by last name')
    print(f'3. {operator} by full name')
    print(f'4. {operator} by telephone number')
    print(f'5. {operator} by city or state')

    search_type = int(input(f'Enter the number of {operator} type: '))
    return search_type


def search_contact():
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


def display_one_contact(contact):
    for k, v in contact.items():
        print(k.capitalize(), ':', v.upper())
    print('--------------')


def create_new_contact():
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


def add_new_contact():
    new_char = create_new_contact()
    contact_book['contacts'].append(dict(new_char))
    rewrite_json()
    print('New contact added')
    menu()


def delete_contact():
    print('Please enter the number of contact you want to remove: ')
    fullname_list()
    rem_cont = int(input('')) - 1
    display_one_contact(contact_book['contacts'][rem_cont])
    really = input('Do really want to remove this contact? y/n')
    if really == 'y':
        contact_book['contacts'].pop(rem_cont)
        rewrite_json()
    menu()


def fullname_list():
    index = 1
    for i in contact_book['contacts']:
        for k, v in i.items():
            if k == 'full name':
                print(index, '-', v)
        index += 1


def update_contact():
    print('Please enter the number of contact you want to update: ')
    fullname_list()
    up_cont = int(input('')) - 1
    display_one_contact(contact_book['contacts'][up_cont])
    really = input('Do really want to update this contact? y/n')
    if really == 'y':
        value_update(up_cont)
    menu()


def value_update(up_cont):
    update_type = operator_menu('Update')
    value = str(input('Enter update value: '))
    index = 1
    for k, v in contact_book['contacts'][up_cont].items():
        if index == update_type:
            contact_book['contacts'][up_cont][k] = value
            rewrite_json()
            print('Contact updated')

        index += 1


def exit():
    menu()


if __name__ == '__main__':
    c = menu()









