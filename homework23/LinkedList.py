
# Extend UnorderedList
# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position and going up to but not including the stop position.

from node import Node

class UnorderedList:

    def __init__(self):
        self.__head = None

    def append(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
            return
        last_node = self.__head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def index(self, some_data):
        position = 0
        current = self.__head
        existence = False
        while current is not None and not existence:
            if current.data == some_data:
                existence = True
            else:
                current = current.next_node
                position += 1
        if not existence:
            raise ValueError('There is no such value!')
        return position

    def list_len(self):
        current = self.__head
        length = 0
        while current is not None:
            length += 1
            current = current.next_node
        return length

    def pop(self, index = None):
        current_node = self.__head
        current_index = 0
        if index is None:
            while current_node.next_node:
                prev_node = current_node.next_node
                if current_node.next_node.next_node == None:
                    current_node.next_node = None
                else:
                    current_node = current_node.next_node
            return prev_node.data
        if index >= self.list_len():
            raise IndexError('Index out of range!')
        if index == 0:
            head = self.__head
            self.__head = self.__head.next_node
            return head.data
        while True:
            prev_node = current_node.next_node
            last_node = current_node
            current_node = current_node.next_node
            if current_index == index - 1:
                last_node.next_node = current_node.next_node
                return prev_node.data
            current_index += 1

    def insert(self, index, data):
        current = self.__head
        if current is None:
            raise ValueError("Linked list is empty")
        if index > self.list_len():
            raise IndexError('Index out of range!')
        counter = 0
        while current:
            if counter == index - 1:
                current.next_node = Node(data, current.next_node)
                break
            current = current.next_node
            counter += 1

    def slice(self, start_index, stop_index):
        new_linked_list = UnorderedList()
        current = self.__head
        current_index = 0
        if current is None:
            raise ValueError("Linked list is empty")
        if start_index > stop_index:
            raise IndexError('Start index cannot be bigger than finish index')
        while current:
            if current_index >= start_index and current_index <= stop_index:
                new_linked_list.append(current.data)
            current_index += 1
            current = current.next_node
        return new_linked_list.display()

    def display(self):
        print(self.__head)


if __name__ == '__main__':
    s = UnorderedList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append('sad')
    s.display()
    # print(s.slice(7,3)) Тут проверял что если старт больше финиша - ВСЕ ХОРОШО)
    s.insert(3, 5)
    s.display()
    s.slice(2,3)
    s.display()
    print(s.pop())
    s.display()
    print(s.pop(2))
    s.display()
    print(s.pop(0))
    s.display()
    print(s.pop(0))
    s.display()
    # print(s.pop()) # Если так попнуть последний элемент то выдает ошибку!!!!!!!!!!!! СДЕСЬ ВОПРОС :(
    print(s.pop(0)) # Если так попнуть последний элемент то все работает и возвращает None
    s.display()
    # s.slice(0,2) Тут проверял ошибку что если линкедлист пустой,то слайс не работает - ВСЕ ХОРОШО)
