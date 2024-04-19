def fib(number):
    a = 0
    b = 1

    for i in range(number):
        yield a     # we can use yield because everytime we call the function we gonna yield the value a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)
