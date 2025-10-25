def find_insert_position(sorted_list, value):
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            return i  # позиція перед більшим елементом
    return len(sorted_list)  # якщо елемент найбільший — в кінець

#Тест 
numbers = [1, 3, 5, 7, 9]
print("Список: {numbers}")

x = int(input("Введіть число для вставки: "))
pos = find_insert_position(numbers, x)

print("Позиція для вставки: {pos}")
numbers.insert(pos, x)
print("Новий список: {numbers}")
