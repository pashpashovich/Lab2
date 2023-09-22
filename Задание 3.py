def find_negative_column(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        all_negative = True  # Предполагаем, что все элементы отрицательны
        column_sum = 0  # Сумма элементов в столбце
        count = 0  # Количество элементов в столбце

        for row in range(rows):
            if matrix[row][col] >= 0:
                all_negative = False
                break  # Если найден положительный элемент, выходим из цикла
            else:
                column_sum += matrix[row][col]
                count += 1

        if all_negative:
            # Если все элементы в столбце отрицательны, вычисляем среднее арифметическое
            if count > 0:
                avg = column_sum / count
            else:
                avg = 0  # Защита от деления на 0, если столбец пустой
            return col, avg

    return None, None  # Возвращаем None, если не найден столбец с отрицательными элементами


# Пример использования
matrix = [
    [1, -2, -3],
    [4, -5, -6],
    [7, -8, -9]
]

column_index, average = find_negative_column(matrix)

if column_index is not None:
    print(f"Первый столбец с отрицательными элементами: {column_index + 1}")
    print(f"Среднее арифметическое элементов в этом столбце: {average}")
else:
    print("В матрице нет столбца, где все элементы отрицательны.")
