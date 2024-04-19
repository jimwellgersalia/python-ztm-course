def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))

# This function is a pure function
# Because if we gave the input it will return the same output no matter how many times running
# This function doesnt produce side effect because we not affecting anything in outside world
# if you put print inside the function it interacts in outside world.
