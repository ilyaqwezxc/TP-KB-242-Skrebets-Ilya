# Програма тестування методів списків 

print("Тестування функцій списків у Python")

# Початковий список
numbers = [5, 2, 9, 1]
print("Початковий список: {numbers}")

# append – додає елемент у кінець списку
numbers.append(7)
print("Після append(7): {numbers}")

# extend – додає кілька елементів одразу (інший список)
numbers.extend([3, 8])
print("Після extend([3, 8]): {numbers}")

# insert(index, value) – вставляє елемент у певну позицію
numbers.insert(2, 10)  # вставляємо 10 на позицію 2
print("Після insert(2, 10): {numbers}")

# remove(value) – видаляє перший елемент із заданим значенням
numbers.remove(9)
print("Після remove(9): {numbers}")

# sort – сортує список за зростанням
numbers.sort()
print("Після sort(): {numbers}")

# reverse – перевертає порядок елементів
numbers.reverse()
print("Після reverse(): {numbers}")

# copy – створює копію списку
copy_list = numbers.copy()
print("Копія списку через copy(): {copy_list}")

# clear – очищує список повністю
numbers.clear()
print("Після clear(): {numbers}")
