from random import randint

num = input('Number: ')
times_looped = 0

while num != 1:
    if num == 'random':
        num = randint(1 - 1000)

    else:
        num = int(num)
    if num % 2 == 0:
        num = num / 2

    else:
        num = num * 3 + 1

    times_looped += 1
    print(num)

print(times_looped)
input('...')
