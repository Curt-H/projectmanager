from time import time, localtime, strftime


def format_time(now=localtime(), time_format=''):
    if time_format == '':
        time_format = '[%Y|%m|%d|%a|%H:%M:%S]:'
    return strftime(time_format, now)


def log(*args, **kwargs):
    dt = format_time()
    print(dt)
    print(*args, **kwargs)

    with open('log.txt', 'a+') as f:
        print(dt, file=f)
        print(*args, **kwargs, file=f)
