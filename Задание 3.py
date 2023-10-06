import random


def print_matrix(matrix):
    for row in matrix:
        row_str = " ".join(map(str, row))  # Преобразование чисел в строки и объединение элементов строки через пробел
        print(row_str)


def generate_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = random.randint(-100, 100)  # Генерация случайного числа от -100 до 100
            row.append(value)  # вставляем значение в столбец
        matrix.append(row)  # вставляем столбцы в матрицу
    return matrix


def find_negative_column(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for col in range(cols):
        all_negative = True
        column_sum = 0
        count = 0
        for row in range(rows):
            if matrix[row][col] >= 0:
                all_negative = False
                break
            else:
                column_sum += matrix[row][col]
                count += 1

        if all_negative:
            if count > 0:
                avg = column_sum / count
            else:
                avg = 0
            return col, avg

    return None, None


def input_matrix():
    while True:
        try:
            choice = int(
                input("Хотите ввести собственные значения (нажмите 1) или сгенерировать случайные (нажмите 2)? "))
            if choice == 1 or choice == 2:
                break
        except ValueError:
            print("Неверный ввод... Повторите попытку")
    try:
        if choice == 1:
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            matrix = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    value = int(input(f"Введите значение для [{i + 1}][{j + 1}]: "))
                    row.append(value)
                matrix.append(row)
        else:
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            matrix = generate_random_matrix(rows, cols)

        return matrix
    except ValueError:
        print("Ошибка: Введите целые числа для размеров матрицы и элементов.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Пример использования
while True:
    user_matrix = input_matrix()
    print_matrix(user_matrix)
    if user_matrix is not None:
        column_index, average = find_negative_column(user_matrix)
        if column_index is not None:
            print(f"Первый столбец с отрицательными элементами: {column_index + 1}")
            print(f"Среднее арифметическое элементов в этом столбце: {average}")
        else:
            print("В матрице нет столбца, где все элементы отрицательны.")
        break  # Выход из цикла после успешного ввода
