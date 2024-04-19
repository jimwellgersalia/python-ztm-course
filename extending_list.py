class SuperList(list):  # now list is our parent class, we can use all the methods now that list have
    def __len__(self):
        return 1000


super_list1 = SuperList()


print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
