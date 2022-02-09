class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        if self.next_node:
            return f'{self.data}->{self.next_node}'
        else:
            return f'{self.data}->|'

