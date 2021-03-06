# Task 1
# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for it in range(len(iterable)):
        yield start + it,iterable[it]


for i in with_index([1,2,3,4,5]):
    print(i)

# Task 2
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

def in_range(start, end=None, step=None):
    if end == None:
        end = start
    if step == None:
        step = 1
    while True:
        if step > 0 and start >= end:
            break
        elif step < 0 and start <= end:
            break
        yield start
        start += step
ran1 = in_range(-3,-1)
for i in ran1:
    print(i)
ran2 = in_range(0,30,5)
for i in ran2:
    print(i)

# Task 3
# Create your own implementation of an iterable,
# which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax.

class Iter:
    def __init__(self, data):
        self.__data = data
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        try:
            return self.__data[self.__index - 1]
        except IndexError:
            self.__index = 0
            raise StopIteration

    def __getitem__(self, item):
        return self.__data[item]




l = Iter('qwerty')
for i in l:
    print(i)








