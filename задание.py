def count_letter_pairs(input_string):
    lower_pairs = 0
    upper_pairs = 0

    i = 0
    while i < len(input_string) - 1:
        if input_string[i].islower() and input_string[i + 1].islower():
            lower_pairs += 1
            i += 2
        elif input_string[i].isupper() and input_string[i + 1].isupper():
            upper_pairs += 1
            i += 2
        else:
            i += 1

    return lower_pairs, upper_pairs


# Пример использования
input_str = input("Введите строку: ")
lower, upper = count_letter_pairs(input_str)
print(f"Пары нижнего регистра: {lower}")
print(f"Пары верхнего регистра: {upper}")
