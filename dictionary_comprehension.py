simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
my_dict2 = {key: value**2 for key, value in simple_dict.items() if value %
            2 == 0}
my_dict3 = {k: k*2 for k in [1, 2, 3]}

print(my_dict)
print(my_dict2)
print(my_dict3)
