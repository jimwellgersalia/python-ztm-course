# with open('test.txt', mode='r+') as my_file: -------- this read and write the file overwriting whatever is in the first characters of a file
# with open('test.txt', mode='w') as my_file:  ---------- this write the file and will create a file if it doesnt exist and overwrite the entire file if it exist
with open('app/sad.txt', mode= 'r') as my_file:
    # print(my_file.read())
    # print(my_file.readline())
    # print(my_file.readline())
    # print(my_file.readline())
    # print(my_file.readlines())
    print(my_file.read())
