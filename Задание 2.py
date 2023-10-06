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


while True:  # цикл запроса ввода
    try:
        print("1.Список\n2.Словарь\n3.Целое число\n4.Строка")
        a = int(input("Выберите тип данных для использования, введя его порядковый номер: "))
        if 0 < a < 5:
            break
        else:
            print("Значение должно быть в диапазоне от 1 до 4... Повторите попытку")
    except ValueError:
        print("Неверный ввод... Повторите попытку")

input_data = None
try:
    while True:
        try:
            choice = int(input(
                "Если хотите использовать тестовые значения, нажмите 1, если хотите сами вводить данные, то нажмите 2: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Значение должно быть в диапазоне от 1 до 2... Повторите попытку")
        except ValueError:
            print("Неверный ввод... Повторите попытку")

    if a == 1:
        if choice == 1:
            input_list = [1, 2, 3, 4, -5, 6, 7, -8]
            print(f"Тестовые значения: {input_list}")
        else:
            # Запрос у пользователя на ввод
            user_input = input("Введите список: ")
            input_list = [int(x) for x in user_input.split()]
        print(
            "Задание: найти количество четных чисел. Вывести максимальное число. Удалить все отрицательные элементы из списка.")
        print("Результат: ", process_input(input_list))
    elif a == 2:
        if choice == 1:
            input_dict = {"a": 5, "b": 3, "c": 7}
            print(f"Тестовые значения: {input_dict}")
        else:
            user_input = input("Введите данные в формате ключ1:значение1, ключ2:значение2: ")
            input_dict = dict(item.split(":") for item in user_input.split(", "))
        print("Задание: отсортируйте по значению в порядке убывания")
        print("Результат: ", process_input(input_dict))
    elif a == 3:
        if choice == 1:
            input_num = 12345
            print(f"Тестовое значение: {input_num}")
        else:
            user_input = input("Введите целое число: ")
            input_num = int(user_input)
        print("Задание: вывести в обратном порядке")
        print("Результат: ", process_input(input_num))
    elif a == 4:
        if choice == 1:
            input_str = "hello world"
            print(f"Тестовое значение: {input_str}")
        else:
            user_input = input("Введите строку: ")
            input_str = int(user_input)
        print("Задание: определить количество вхождений каждого символа. Вывести в виде словаря")
        print("Результат: ", process_input(input_str))
    else:
        print("Неподдерживаемый тип данных")
        input_data = None
    if input_data is not None:
        result = process_input(input_data)
        print(result)

except ValueError:
    print("Ошибка: неверный формат ввода.")
