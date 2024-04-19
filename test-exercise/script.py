from random import randint


def run_guess(guess, answer):
    if 1 <= guess <= 10:
        if answer == guess:
            print('Congratulations you guess the number! You are genius')
            return True
    else:
        print(f'Please enter a number between 1 to 10 only.')
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input(f'Please guess a number between 1 to 10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter a number only')
            continue
