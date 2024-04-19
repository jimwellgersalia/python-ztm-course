while True:
    try:
        age = int(input('Please enter your age: '))
        # print(age)
        10/age
    except ValueError:  # except without a error name can catch all the error of the program and return the statement inside of it
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter number higher than 0')
    else:
        print('Thank you')
        break
