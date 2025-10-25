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

# Введення чисел користувачем
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# --- Виконання вибраної операції ---
if choice == '1' or choice == '+':
    print("Результат: {add(a, b)}")

elif choice == '2' or choice == '-':
    print("Результат: {subtract(a, b)}")

elif choice == '3' or choice == '*':
    print("Результат: {multiply(a, b)}")

elif choice == '4' or choice == '/':
    print("Результат: {divide(a, b)}")

else:
    print("Невірний вибір операції!")
