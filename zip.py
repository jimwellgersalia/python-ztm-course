my_list = [1, 2, 3,]
your_list = [10, 20, 30]

# again we create a zip object and store it in the memory.
# what it does is it take the value of the 1st item of first list
# and combine it to the first item of the second list and turn it into a tuple
# we can do this not only in list but to all iterables.
print(zip(my_list, your_list))
print(list(zip(my_list, your_list)))
print(my_list)
print(your_list)
