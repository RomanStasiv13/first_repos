def hours_min_sec(h=0, m=0, s=0):
    m += s // 60
    s = s % 60
    h += m // 60
    m = m % 60
    d = 0
    d += h // 24
    h = h % 24
    if d == 0:
        return f'{h:02d}:{m:02d}:{s:02d}'
    return f'{d} days, {h:02d}:{m:02d}:{s:02d}'


def get_positive_number(prompt):
    while True:
        user_time = input(prompt)
        if user_time.isdigit():
            return int(user_time)


def prettify_seconds(s):
    return hours_min_sec(s=s)


if __name__ == '__main__':
    # hours = get_positive_number('hours')
    # minutes = get_positive_number('minutes')
    # seconds = get_positive_number('seconds')

    rez = prettify_seconds(86400)
    print(rez)
