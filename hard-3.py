n = int(input('Введите n: '))
m = int(input('Введите m: '))
for i in range(n):
    if i % 2 == 0:
        print(m * "AAABBB")
    else:
        print(m * "BBBAAA")
