# Програма тестування функцій словників

print("Тестування функцій словників у Python")

# Початковий словник
student = {
    "name": "Іван",
    "age": 18,
    "grade": "A"
}
print("Початковий словник: {student}")

# update – оновлює або додає нові пари ключ-значення
student.update({"age": 19, "city": "Київ"})
print("Після update(): {student}")

# del – видаляє елемент за ключем
del student["grade"]
print("Після del student['grade']: {student}")

# keys – повертає всі ключі словника
print("Ключі словника (keys()): {list(student.keys())}")

# values – повертає всі значення словника
print("Значення словника (values()): {list(student.values())}")

# items – повертає всі пари ключ-значення у вигляді кортежів
print("Пари ключ-значення (items()): {list(student.items())}")

# clear – повністю очищує словник
student.clear()
print("Після clear(): {student}")
