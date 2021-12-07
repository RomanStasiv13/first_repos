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

# def add_new(char):
#     contact_list = []
#     for i in range(len(char[0])):
#         if i==0:
#             contact_list.append(str(input('Enter the first name: ')).lower().capitalize())
#         if i==1:
#             contact_list.append(str(input('Enter the last name: ')).lower().capitalize().lower().capitalize())
#         if i==2:
#             contact_list.append(str(input('Enter the telephone number: ')))
#         if i==3:
#             contact_list.append(str(input('Enter the state/city of living: ')).lower().capitalize())
#         if i==4:
#             contact_list.append(str(input('Other options e-mail/company/family etc.: ')))
#     char.append(contact_list)
#     return char
#     pass
#
# def search_by_fn():
#
#     pass
#
# def search_by_ln():
#     pass
#
# def search_by_fulln():
#     pass
#
# def search_by_num():
#     pass
#
# def search_by_state():
#     pass
#
# def delete_rec(char):
#     contact_del = str(input('Enter the fullname of the contact you wish to remove: ')).lower().capitalize()
#     del_char = 0
#     for i in range(len(char)):
#         if contact_del == char[i][0]:
#             del_char += 1
#             print(char.pop(i))
#             print('This contact has now been removed')
#             return char
#     if del_char==0:
#         print('Something get wrong')
#         return char
#
#     pass
#
# def update_rec():
#     pass
#
# def contact_menu():
#     print('\t Please,choose the operation:\n')
#     print('1.Add new entries')
#     print('2.Search by first name')
#     print('3.Search by last name')
#     print('4.Search by full name')
#     print('5.Search by telephone number')
#     print('6.Search by city or state')
#     print('7.Delete a record for a given telephone number')
#     print('8.Update a record for a given telephone number')
#     print('9.Exit from contacts')
#
#     choice = int(input('Enter the number of your choice: '))
#     return choice
#
# def exit():
#     pass
#
#
# if __name__ == '__main__':

### Еще не успел доделать из-за работы остальное :(


