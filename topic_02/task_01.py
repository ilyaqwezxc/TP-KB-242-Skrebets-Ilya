
import math

# Функція для обчислення дискримінанта
def discriminant(a, b, c):
    return b**2 - 4*a*c

# Функція для знаходження коренів квадратного рівняння
def quadratic_roots(a, b, c):
    D = discriminant(a, b, c)  # Викликаємо функцію обчислення дискримінанту
    print("Дискримінант D = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Два різних корені: x₁ = {x1}, x₂ = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print("Один корінь: x = {x}")
    else:
        print("Рівняння не має дійсних коренів")

# Основна частина програми 
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

quadratic_roots(a, b, c)
