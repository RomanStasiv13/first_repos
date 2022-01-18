import sys
def count_lines(name):
    with open(f'{name}', 'r') as fp:
        count = 0
        for lines in fp:
            count += 1
        return count

def count_chars(name):
    char_counter = 0
    with open(f'{name}', 'r') as fp:
        for line in fp:
            char_counter += len(line)
        return char_counter

actions = {'-c':count_chars,
           '-l':count_lines}

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] in actions:
            func = actions[sys.argv[1]]
            func(sys.argv[2])