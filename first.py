data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    import re
    str_data = str(data_structure)  # перевод в строку
    numbers = re.findall(r'\d+', str_data)  # извлечение цифр из строки в список
    letters = "".join(c for c in str_data if c.isalnum())  # избавляюсь от не цифр и не букв
    str2 = ''
    for i in letters:
        if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            str2 = str2 + i
    result = sum(list(map(int, numbers))) + len(str2)
    print(result)
result = calculate_structure_sum(data_structure)


# Не совсем понятно, почему из 'Urban2' никак не извлекается двойка(2).
# Ведь в задании сказано "Все числа (не важно, являются они ключами или значениям или ЕЩЕ ЧЕМ-ТО)."
# Считаю, что ответ 100 верный.