import re

# pattern = re.compile(
#     r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.* ).{8,16}$') # this one is the legit password validation but for the sake of exercise

# andrei only asks
# At least 8 char long
# contain any sort letters, numbers, $%#@
# has to end with a number
pattern = re.compile(r'[a-zA-z0-9$%#@]{8,}[0-9]')

password = 'hh12321321j1'
check = pattern.fullmatch(password)

print(check)

# while True:
#     password = input('Please input a password: ')
# match_pattern = pattern.fullmatch(password)
# if match_pattern:
#     print('Congrats. You enter a strong password.')
#     break
# else:
#     print('Please enter 8-16 character with lowercase, uppercase, numbers and punctuation combined. Try again')
