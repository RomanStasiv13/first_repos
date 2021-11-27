if __name__ == '__main__':
    ###Task 1
    ###The greatest number
    ###Write a Python program to get the largest number from a list of random numbers with the length of 10
    ###Constraints: use only while loop and random module to generate numbers
    import random
    my_list = random.sample(range(0,50),10)
    print(my_list)
    i = 0
    largest_num = my_list[i]
    while i < len(my_list):
        if my_list[i] > largest_num:
            largest_num = my_list[i]
        i = i + 1
    print(largest_num)

    ###Task 2
    ###Exclusive common numbers.
    ###Generate 2 lists with the length of 10 with random integers from 1 to 10,
    ###and make a third list containing the common integers between the 2 initial lists without any duplicates.
    ###Constraints: use only while loop and random module to generate numbers.

    my_list1 = random.sample(range(0,10),10)
    my_list2 = random.sample(range(0,10),10)
    total_list=[]
    print(my_list1)
    print(my_list2)
    i1=0
    i2=0
    while i1<len(my_list1) and i2<len(my_list2):
        if my_list1==my_list2:
            total_list.append(my_list1[i1])
            i1+=1
            i2+=1
        elif my_list1[i1]>my_list2[i2]:
            i2+=1
        else:
            i1+=1
        print(total_list)

    ###Task 3
    ###Extracting numbers.
    ###Make a list that contains all integers from 1 to 100,
    ### then find all integers from the list that are divisible by 7 but not a multiple of 5,
    ###and store them in a separate list. Finally, print the list.
    ###Constraint: use only while loop for iteration

    some_list = list(range(1,101))
    new_list=[]
    j=0
    while j<len(some_list):
        if some_list[j]%7==0 and some_list[j]%5!=0:
            new_list.append(some_list[j])
            j+=1
        else:
            j+=1
    print(new_list)


    ###Рандом и расширение списка.
    ###Заполните лист 10ю рандомными значениями в промежутке 1-100.
    ###(Испольуя метод randint модуля random) Пока длинна листа меньше 10ти добавляйте к листу элемент.
    ###Пройдитесь циклом и найдите минимальное и максимальное значение Не используя встроенные методы.
    ###Выведете минимальное и максимальное значение списка используя встроенные методы.


    ###Преобразование типов и слайсы.
    ###Превратите полученную от пользователя строку в тапл.
    ###Выведите строку содержащую только буквы на четных позициях.

    user_word = input('Enter the word')
    new_word = tuple(user_word,)
    print(new_word[1::2])

    ###