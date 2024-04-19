from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()  # time before running function
        result = func(*args, **kwargs)
        t2 = time()  # time after running function
        print(f'took {t2-t1} s')  # minus them to get the result
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()
