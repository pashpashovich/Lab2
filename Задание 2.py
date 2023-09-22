def process_input(input_data):
    if isinstance(input_data, list):
        # Найти количество четных чисел
        even_count = sum(1 for num in input_data if num % 2 == 0)

        # Вывести максимальное число
        max_num = max(input_data)

        # Удалить отрицательные элементы из списка
        input_data = [num for num in input_data if num >= 0]

        return f"Четные числа: {even_count}, Максимальное число: {max_num}, Список без отрицательных: {input_data}"

    elif isinstance(input_data, dict):
        # Отсортировать словарь по значению в порядке убывания
        sorted_dict = dict(sorted(input_data.items(), key=lambda item: item[1], reverse=True))

        return sorted_dict

    elif isinstance(input_data, int):
        # Вывести число в обратном порядке
        reversed_num = int(str(input_data)[::-1])

        return reversed_num

    elif isinstance(input_data, str):
        # Определить количество вхождений каждого символа и вывести в виде словаря
        char_count = {}
        for char in input_data:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        return char_count

    else:
        return "Неподдерживаемый тип данных"


# Примеры использования функции
input_list = [1, 2, 3, 4, -5, 6, 7, -8]
print(process_input(input_list))

input_dict = {"a": 5, "b": 3, "c": 7}
print(process_input(input_dict))

input_num = 12345
print(process_input(input_num))

input_str = "hello world"
print(process_input(input_str))
