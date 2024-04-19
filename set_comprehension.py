#although this is good. but if you dont know comprehension its a bit confusing.
# So the best thing is you might want to create a function that for example generate list of even numbers etc etc

my_list = {char for char in 'hello'}
my_list2 = {num for num in range(100)}
my_list3 = {num**2 for num in range(100)}
my_list4 = {num**2 for num in range(100) if num % 2 == 0}


# print(my_list)
# print(my_list2)
# print(my_list3)
print(my_list4)
