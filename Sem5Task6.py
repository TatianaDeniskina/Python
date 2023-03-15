from random import randint
print('Угадайте число:')
n = randint(0, 100)
i = 0
while True:
    a = int(input())
    if a == n:
        print('You win!')
        break
    if a < n:
        print('загаданное число больше')
    else:
        print('загаданное число меньше')
    i += 1
    if i == 10:
        print(f'Вы проиграли. Загаданное число {n}')
        break