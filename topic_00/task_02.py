def Diskriminant(a, b, c):
    D = b*b - 4*a*c
    return D

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

D = Diskriminant(a, b, c)
print("Ваш результат:", D)
