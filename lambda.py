from functools import reduce
my_list = [1, 2, 3]

# so we dont need all of these function if we want to use a function only ones. then we can just use lambda


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


# lambda behave like a function but it automatically returns and it will not be saved on to computer memory
print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
