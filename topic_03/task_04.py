def find_insert_position(sorted_list, value):
    for i, v in enumerate(sorted_list):
        if value < v:
            return i
    return len(sorted_list)  # вставка в кінець

my_list = [1, 3, 5, 7]
new_value = 4
position = find_insert_position(my_list, new_value)
print(f"Новий елемент {new_value} потрібно вставити на позицію {position}")
