if __name__ == '__main__':
    ###Task 1
    ###Make a program that has some sentence (a string) on input
    ###and returns a dict containing all unique words as keys and the number of occurrences as values.
    sentence = input('')
    new_dict ={}
    for word in set(sentence.lower().split()):
        if word not in new_dict:
            new_dict[word] = 1
        else: new_dict[word] +=1
    print(new_dict)


    ###Task 2
    ###Create a function which takes as input two dicts with structure mentioned above,
    ###then computes and returns the total price of stock.

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    total = 0
    for key in prices:
        value = prices[key] * stock[key]
        total = total + value
    print(f'Total sum of stock: {int(total)}')

###Task 3
    ###List comprehension exercise
    ###Use a list comprehension to make a list containing tuples (i, j)
    ###where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

    list_of_tuples=[(i,pow(i, 2)) for i in range(1,10) ]
    print(list_of_tuples)
