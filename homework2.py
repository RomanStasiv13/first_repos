###Task 1
###String manipulation
###Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
###If the string length is less than 2, return instead of the empty string.
###Sample String: 'helloworld'
###Expected Result : 'held'
###Sample String: 'my'
###Expected Result : 'mymy'
###Sample String: ' x'
###Expected Result: Empty String
###Tips:
###Use built-in function len() on an input string
###Use positive indexing to get the first characters of a string and negative indexing to get the last characters

input_str = 'Hello wold!'

if len(input_str) < 2:
    print('')
else:
    print(input_str[0:2] + input_str[-2:])

###Task 2
###The valid phone number program.
###Make a program that checks if a string is in the right format for a phone number.
###The program should check that the string contains only numerical characters and is only 10 characters long.
###Print a suitable message depending on the outcome of the string evaluation.

user_phone_num = input('Your phone number,please')

if user_phone_num.isdigit() and len(user_phone_num) == 10:
    if int(user_phone_num[1:3])==96 or int(user_phone_num[1:3])==67 or int(user_phone_num[1:3])==97:
       print('Your number is valid and it is Kievstar')

    elif int(user_phone_num[1:3])==50 or int(user_phone_num[1:3])==95 or int(user_phone_num[1:3])==66:
       print('Your number is valid and it is Vodaphone')

    elif int(user_phone_num[1:3])==63 or int(user_phone_num[1:3])==93 or int(user_phone_num[1:3])==73:
       print('Your number is valid and it is Lifecell:)')
else:
    print('Incorrect number.Please try again!')

###Task 3
###The name check.
###The program should check if your input is equal to the stored name even
###if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
tries = 0
while True and tries<=3:
    name=input('What is your name?')
    tries+=1
    if name.lower()==('roman'):
        print('Correct name')
        break
    elif name.lower()!=('roman') and tries>=3:
        print('Please,try again for 3 seconds')
        import time
        time.sleep(3)




