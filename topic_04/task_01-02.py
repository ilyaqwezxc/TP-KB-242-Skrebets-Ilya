# Функції для арифметичних операцій

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:  # обробка ділення на нуль
        return "Помилка: ділення на нуль!"

# Функція для вводу чисел 
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть правильне число!")

# Основна частина програми

print("Простий калькулятор з обробкою винятків")
print("Введіть 'exit' щоб завершити програму.")

while True:
    print("\nОберіть операцію:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")

    choice = input("Введіть номер або символ операції: ").lower()

    # Перевірка на вихід
    if choice == "exit" or choice == "вихід":
        print("Програма завершена. До побачення!")
        break

    # Введення чисел з обробкою помилок
    a = input_number("Введіть перше число: ")
    b = input_number("Введіть друге число: ")

    # Виконання операції з match-case
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
