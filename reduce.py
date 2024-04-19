from functools import reduce
my_list = [1, 2, 3]


def accumulator(acc, item):
    # base on this function we add all the items in my_list, to reduce it to single value.
    # we can do anything we want to reduce.
    return acc + item


# we also dont need to convert it to list to print out because reduce does it underneath the hood.
# so it displays the single value that we accumulated
print(reduce(accumulator, my_list))  # default accumulator value is 0
# but we can assign to it like this example
print(reduce(accumulator, my_list, 10))
