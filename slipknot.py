import random
import math

def draw_gallow(rest):
    gallows = """___$$$$$$$$$$______Я-ВИСЕЛИЦО!________
___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
______Z___________________$$$$$$$______
______Z___________________$$$$$$$______
______Z___________________$$$$$$$______
_____$$$__________________$$$$$$$______
____$$$$$_________________$$$$$$$______
_____$$$__________________$$$$$$$______
___$ZZZZZ$________________$$$$$$$______
__$$$$$$$$$_______________$$$$$$$______
__$_$$$$$_$_______________$$$$$$$______
__$_$$$$$_$_______________$$$$$$$______
__$_$$$$$_$_______________$$$$$$$______
____$$_$$_________________$$$$$$$______
___$$___$$________________$$$$$$$______
___$$___$$________________$$$$$$$______
___$$___$$_____________$$$$$$$$$$$$$___
$__$$___$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$
_\_________/_______$$$$$$$$$$$$$$$$$$$$$
__\_______/________$$$$$$$$$$$$$$$$$$$$$
__________________$$$$$$$$$$$$$$$$$$$$$
__________________$$$$$$$$$$$$$$$$$$$$$
"""
    draw_percentage = 100 - rest*10
    total_lines_in_gallows = gallows.count("\n")
    display_lines = math.ceil(draw_percentage*total_lines_in_gallows // 100)
    lines = gallows.split('\n')[:display_lines]
    print('\n'*150)
    print('\n'.join(lines))

words=['sister']
tries = 10
if __name__ == '__main__':
    print('\n'*150)
    random_word = random.choice(words)
    shown_word = '*'*len(random_word)
    letters = []
    print(f'Я загадал слово: {shown_word}')

    while '*' in shown_word and tries>0:
       draw_gallow(tries)

       users_letter = input(f'{shown_word} Введите букву: ').strip().lower()

       if not users_letter:
           continue
       users_letter = users_letter[0]
       if users_letter not in random_word:
           tries-=1
           print(f'Осталось попыток: {tries}')
       letters.append(users_letter)
       shown_word = ''.join([l if l in letters else '*' for l in random_word]) ### вместо этого можно ниже

 ##      for l in random_word:
 ##          if l in letters:
 ##              shown_word += l
 ##          else:
 ##              shown_word+= '*'
    if '*' not in shown_word:
        print(f'You won, {shown_word}')
    else:
        print('You lose')