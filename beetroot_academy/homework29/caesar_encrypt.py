import string


def encrypt(text: str, shift: int):
    new_word: str = ''
    text = text.strip()
    for i in range(len(text)):
        letter = text[i]
        if letter not in string.ascii_letters:
            raise ValueError(f'Use only letters: {string.ascii_letters}')
        if letter.isupper():
            new_word += chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            new_word += chr((ord(letter) + shift - 97) % 26 + 97)
    return new_word


# c = encrypt('Roman',6)
# print(c)
# print(type(c))


