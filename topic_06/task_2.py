students_data = [
    {'name': 'Egor', 'grade': 89},
    {'name': 'Roman', 'grade': 76},
    {'name': 'Natali', 'grade': 70},
    {'name': 'Max', 'grade': 96},
    {'name': 'Ihor', 'grade': 63},
    {'name': 'Kirill', 'grade': 70},
    {'name': 'Tom', 'grade': 81},
    {'name': 'Dmitro', 'grade': 95},
    {'name': 'Sasha', 'grade': 80},
    {'name': 'Ivan', 'grade': 91}
]

while True:
    c = input("Обери варіант сортування: name або grade: ").strip().lower()
    if c == "name" or c == "grade":
        break
    else:
        print("\n Помилка,дані введено некоректно!\n")

def sort_dicts(list_dicts, column):
    # Сортування за допомогою sorted() + lambda
    sorted_list = sorted(list_dicts, key=lambda item: item[column])

    if column == "grade":
        print("\Сортувакння за оцінкою: \n")
        sorted_list.reverse()            
    else:
        print("\nСортування за ім'ям: \n")

    # Вивід результату
    for elem in sorted_list:
        print(f'{elem["name"]} {elem["grade"]}')

sort_dicts(students_data, c)
