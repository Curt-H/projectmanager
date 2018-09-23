from time import time, localtime, strftime


def format_time(now=localtime(), time_format=''):
    if time_format == '':
        time_format = '[%Y|%m|%d|%a|%H:%M:%S]:'
    return strftime(time_format, now)


def log(*args, **kwargs):
    dt = format_time()
    print(dt)
    print('[arguements:]', *args, sep='\n')
    print('[keyword arguements:]', *kwargs.items(), sep='\n')
    print('=' * 50)

    with open('log.txt', 'a+', encoding='utf-8') as f:
        print(dt, file=f)
        print('[arguements:]', *args, sep='\n', file=f)
        print('[keyword arguements:]', *kwargs.items(), sep='\n', file=f)
        print('=' * 50, file=f)
