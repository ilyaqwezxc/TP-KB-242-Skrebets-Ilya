my_dict = {"a": 1, "b": 2}
print("Початковий словник:", my_dict)

# update
my_dict.update({"c": 3})
print("update({'c':3}):", my_dict)

# keys
print("keys():", list(my_dict.keys()))

# values
print("values():", list(my_dict.values()))

# items
print("items():", list(my_dict.items()))

# del
del my_dict["a"]
print("del my_dict['a']:", my_dict)

# clear
my_dict.clear()
print("clear():", my_dict)
