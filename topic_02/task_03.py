# Функції для арифметичних операцій 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"

# Основна частина програми

print("Простий калькулятор")
print("Оберіть операцію:")
print("1. Додавання (+)")
print("2. Віднімання (-)")
print("3. Множення (*)")
print("4. Ділення (/)")

choice = input("Введіть номер або символ операції: ")

# Введення чисел
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Виконання операції через match-case 
match choice:
    case "1" | "+":
        print("Результат: {add(a, b)}")
    case "2" | "-":
        print("Результат: {subtract(a, b)}")
    case "3" | "*":
        print("Результат: {multiply(a, b)}")
    case "4" | "/":
        print("Результат: {divide(a, b)}")
    case _:
        print("Невірний вибір операції!")
