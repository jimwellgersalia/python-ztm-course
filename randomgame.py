from random import randint
from sys import argv

first = int(argv[1])
last = int(argv[2])

answer = randint(first, last)

while True:
    try:
        guess = int(
            input(f'Please guess a number between {first} to {last}: '))
        if first <= guess <= last:
            if answer == guess:
                print('Congratulations you guess the number! You are genius')
                break
            else:
                print('Sorry Wrong Answer. Guess the number again')
                continue
        else:
            print(f'Please enter a number between {first} to {last} only.')
            continue

    except ValueError:
        print('Please enter a number only')
        continue
