def div(num1, num2):
    try:
        return num1 / num2
    # useful to combine error if you want to handle them to use in the same way.
    except (TypeError, ZeroDivisionError) as err:
        return (f'Something is wrong \n{err}')


print(div(40, '2'))
print(div(40, 0))
