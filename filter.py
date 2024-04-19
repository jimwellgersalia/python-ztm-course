my_list = [1, 2, 3, 4, 5]


def only_odd(item):
    return item % 2 != 0


# again we create a new filter object so its still pure function because we dont affect the original one
print(filter(only_odd, my_list))
# what filter does is its only return what the conditions is in the function.
print(list(filter(only_odd, my_list)))
print(my_list)
