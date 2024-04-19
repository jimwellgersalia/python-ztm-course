some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# very long and so confusing one line set of code
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))


print(duplicates)
