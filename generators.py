def generators_function(num):
    for i in range(num):
        # if it has yield it becomes generator. now yield pauses the function. and just comes back to it when we called next
        yield i*2


g = generators_function(100)

next(g)  # this is 0 * 2 the first value of range
next(g)  # this is 1 * 2 the function will continue
print(next(g))  # then this is 2 * 2 the 3rd value.

# now if you exceed the number of items in range you will get StopIteration Error
