import random

min = input('please give a minimum value: ')
max = input('please give a msximum value: ')
min = int(min)
max = int(max)

r = random.randint(min, max)
count = 0

while True:
    count += 1 # count = count + 1
    num = input('guess a number: ')
    num = int(num)
    if num == r:
        print('you get it!')
        print('You have guessed', count, 'times')
        break
    elif num > r:
        print(num, 'is larger')
    else:
        print(num, 'is smaller')
    print('You have guessed', count, 'times')
    