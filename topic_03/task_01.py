def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число!")

print("Калькулятор. Введіть 'exit' щоб завершити.")

while True:
    operation = input("\nОберіть операцію (+, -, *, /): ").lower()
    if operation == "exit":
        print("Програма завершена.")
        break
    a = input_number("Введіть перше число: ")
    b = input_number("Введіть друге число: ")

    match operation:
        case "+":
            print(f"Результат: {add(a, b)}")
        case "-":
            print(f"Результат: {subtract(a, b)}")
        case "*":
            print(f"Результат: {multiply(a, b)}")
        case "/":
            print(f"Результат: {divide(a, b)}")
        case _:
            print("Невірна операція!")
