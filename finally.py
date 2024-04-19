while True:
    try:
        age = int(input('Please enter your age: '))
        # print(age)
        10/age
    except ValueError:  # except without a error name can catch all the error of the program and return the statement inside of it
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter number higher than 0')
    else:
        print('Thank you')
        break
    # finally is very useful when example logging what user does because it always run no matter what.
    finally:  # ignores the break and continue statement, and will still get into statement inside of it even if its not error.
        print('im officially done!!')
