import math
a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x1 = -(b / 2 * a)
    x2 = x1
    print("x1 =", x1)
    print("x2 =", x2)
elif D < 0:
    print("Уравнение не имеет решения")
