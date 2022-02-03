
class Stack:
    def __init__(self):
        self._elements = []

    def is_not_empty(self):
        return bool(self._elements)

    def push(self, elem):
        self._elements.append(elem)

    def pop(self):
        if self._elements:
            return self._elements.pop()
        return None

    def __repr__(self):
        representation = ''
        for i in self._elements:
            representation += i
        return representation

    def __str__(self):
        return self.__repr__()

    # Task 1
    # Write a program that reads in a sequence of characters
    # and prints them in reverse order, using your implementation of Stack.

    def reverse(self):
        copy = self._elements[:]
        reverse = ''
        while self.is_not_empty():
            for i in range(len(copy)):
                reverse += copy.pop()
            return reverse
        return 'Empty Stack'

    # Task 3
    #Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.

    def get_from_stack(self, elem):
        copy = self._elements[:]
        new = ''
        if elem in copy:
            idx = copy.index(elem)
            new += copy.pop(idx)
            return new
        raise ValueError


# Task 2
# Write a program that reads in a sequence of characters, and determines whether it's parentheses,
# braces, and curly brackets are "balanced."

def balanced(string):
    brackets = {
        '(':')',
        '[':']',
        '{':'}'
    }
    queue = []

    for i in string:
        if i in brackets.keys():
            queue.append(brackets[i])
        elif i in brackets.values():
            if not queue or i != queue.pop():
                return f'{string} is unbalanced'
    if not queue:
        return f'{string} is balanced'
    return f'{string} is unbalanced'


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_not_empty())
    print(stack.reverse())
    stack.push('h')
    stack.push('e')
    stack.push('l')
    stack.push('l')
    stack.push('o')
    print(stack)
    print(stack.is_not_empty())
    print(stack.reverse())
    print(stack.get_from_stack('e'))
    #print(stack.get_from_stack('y'))
    print(balanced("{[]{()}}"))
    print(balanced("((0))"))
    print(balanced("(ad(ad}ad]"))
    print(balanced("{]}"))




