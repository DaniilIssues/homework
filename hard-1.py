a = int(input())
b = 1
c = 0
while b <= a:
    if a % b == 0:
        c += 1
    b += 1
if c == 2 or c == 1:
    print("Число", a, "простое")
else:
    print("Число", a, "составное")
