my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


# -  a new object created so were copying it and we dont touch the variable.
print(map(multiply_by2, my_list))
# we need to convert it to list to get it printed because it's an object.
print(list(map(multiply_by2, my_list)))
print(my_list)  # we can see that we didnt affect the value of this variable
