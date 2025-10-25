# Програма тестування методів списків

print("=== Тестування функцій списків у Python ===")

# Початковий список
numbers = [5, 2, 9, 1]
print(f"Початковий список: {numbers}")

# 1️⃣ append – додає елемент у кінець списку
numbers.append(7)
print(f"Після append(7): {numbers}")

# 2️⃣ extend – додає кілька елементів одразу (інший список)
numbers.extend([3, 8])
print(f"Після extend([3, 8]): {numbers}")

# 3️⃣ insert(index, value) – вставляє елемент у певну позицію
numbers.insert(2, 10)  # вставляємо 10 на позицію 2
print(f"Після insert(2, 10): {numbers}")

# 4️⃣ remove(value) – видаляє перший елемент із заданим значенням
numbers.remove(9)
print(f"Після remove(9): {numbers}")

# 5️⃣ sort – сортує список за зростанням
numbers.sort()
print(f"Після sort(): {numbers}")

# 6️⃣ reverse – перевертає порядок елементів
numbers.reverse()
print(f"Після reverse(): {numbers}")

# 7️⃣ copy - створює копію списку
copy_list = numbers.copy()
print(f"Копія списку через copy(): {copy_list}")

# 8️⃣ clear – очищує список повністю
numbers.clear()
print(f"Після clear(): {numbers}")

