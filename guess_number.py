import random

r = random.randint(1, 100)

while True:
    num = input('guess a number: ')
    num = int(num)
    if num == r:
        print('you get it!')
        break
    elif num > r:
        print(num, 'is larger')
    else:
        print(num, 'is smaller')