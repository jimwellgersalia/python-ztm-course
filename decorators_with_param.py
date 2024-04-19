# Decorator Pattern. Can just copy and paste this if youre creating decorator
def my_decorators(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func


@my_decorators  # just add this @and name of func before the function that you want to give decorators to
def hello(greeting='Input a greeting please', emoji= ':('):
    print(greeting, emoji)

hello('Hello, Welcome to Decorators with parameters!', ':*')
hello()
