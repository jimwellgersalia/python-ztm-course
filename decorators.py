# Decorators
# improves readability of a code
# and giving extra functionalities for our function
def my_decorators(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorators  # just add this @and name of func before the function that you want to give decorators to
def hello():
    print('helllloooooooooo')


@my_decorators
def bye():
    print('see ya later')


hello()
bye()
