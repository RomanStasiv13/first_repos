if __name__ == '__main__':


    ###Task 1
    ###The Guessing Game.
    ###Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
    ###The result should be sent back to the user via a print statement

    import random

    tries = 0
    number = (random.randint(1,10))
    print('Hmmmm....Try to guess what number between 1 and 10 I was thinking about :)')
    while tries < 3:
        guess = int(input('Take a guess: '))
        tries += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print(f'Congratulations! You guessed my number in {tries} guesses')
            break
        if guess != number and tries == 3:
            print(f"Sorry, but you didn't make it. My number was: {number}")
            break

    ###Task 2
    ###The birthday greeting program.
    ###Write a program that takes your name as input, and then your age as input and greets you with the following:
    ###“Hello <name>, on your next birthday you’ll be <age+1> years”

    name = input('What is your name?')
    age = input('How old are you?')

    if age.isdigit():
        print(f'Hello {name.lower().capitalize()}, on your next birthday you’ll be {int(age) + 1} years” ')
    else:
        print('Please enter your age in the numerical format')
        age = input("Let's try again.How old are you?")
        if age.isdigit():
            print(f'Hello {name.lower().capitalize()}, on your next birthday you’ll be {int(age) + 1} years” ')

    ###Task 3
    ###Words combination
    ###Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
    ###For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
    ###Tips: Use random module to get random char from string)
    my_string = input('Enter the word')
    word_lenth = 4
    word_number = 5
    while word_number > 0:
        word_number-=1
        new_string = my_string
        word = ''
        while len(word)<word_lenth:
            import random
            index = random.randint(0,len(new_string)-1)
            word += new_string[index]
            new_string=new_string[0:index]+new_string[index+1:]
        print(word)
    ### Task 4
    ###The math quiz program
    ###Write a program that asks the answer for a mathematical expression,
    ###checks whether the user is right or wrong, and then responds with a message accordingly.


    import random
    x1 = random.randint(0,100)
    x2 = random.randint(0,100)
    x3 = random.randint(0,100)
    while True:
        y = x1+x2-x3
        print(f'{x1}+{x2}-{x3}=')
        player_result = int(input('Please,enter the result'))
        if y==player_result:
            print('Right answer!')
            break
        else:
            print('Wrong answer,try again')
        continue


    ###Используя модуль random и его функции randint напишите игру "математика 5кл".
    ###Правила следующие. Есть три разных формулы "y=2x+3" "y=3x+15" "y=x+7"
    # с помощю рандома выберите значение для х в пределах от нуля до 30ти, и одну из формул.
    # Выведите на экран выбранную формулу и значение x, получите ответ и проверьте его правильность
    # (для этого переведите свой ответ в строку и сравните строки). Например х получил значение 5
    # и рандомная формула вторая. Тогда на экран выводится
    ###y=3x+15
    ###x = 5
    ###y = ?
    ###если человек вводит 30 пишем ему "молодец" и заканчиваем игру.
    ###Если другое число - "ты можешь лучше" и загадываем новое х и новую формулу выбираем.
    import random
     y = {1:'y=2x+3', 2:'y=3x+15', 3:'y=x+7'}
     comp_choice = y[random.randint(1,3)]

     x = random.randint(0,30)
     print(f'Введите ответ {comp_choice}, x={x}')
     answer=input(str(''))
      if comp_choice==1:
         if 2*x+3 == int(answer)
           print('Молодец!')
      elif comp_choice==2:
        if 3*x+15 == int(answer):
           print('Молодец!')
      elif comp_choice==3:
        if x+7 == int(answer)
          print('Молодец!')
      else:
        print('Ты можешь лучше!')

    ###combinations из модуля itertools
    ###Получите от пользователя слово длинной больше 5 символов (проверка , цикл пока не введет правильное).
    ###Сгенерируйте и выведите 5 комбинаций которые можно получить переставив буквы в слове (random.choice, pop, while)

    import intertools















