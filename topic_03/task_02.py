my_list = [1, 2, 3]
print("Початковий список:", my_list)

# append
my_list.append(4)
print("append(4):", my_list)

# extend
my_list.extend([5, 6])
print("extend([5,6]):", my_list)

# insert
my_list.insert(2, 99)
print("insert(2,99):", my_list)

# remove
my_list.remove(2)
print("remove(2):", my_list)

# copy
list_copy = my_list.copy()
print("copy():", list_copy)

# reverse
my_list.reverse()
print("reverse():", my_list)

# sort
my_list.sort()
print("sort():", my_list)

# clear
my_list.clear()
print("clear():", my_list)
