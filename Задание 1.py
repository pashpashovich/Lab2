def prime(num):
    i = 0  # номер текущего элемента по счёту
    current = 2  # начинаем с первого простого числа
    while i < num:  # цикл для поиска нужного простого числа
        k = 0
        for t in range(2, current):
            if current % t == 0:  # есть делитель
                k = 1
                break
        if k == 0:  # нашли простое число
            i = i + 1
        current = current + 1  # идём к следующему числу
    return current - 1


while True:  # цикл запроса ввода
    try:
        a = int(input("Введите номер простого числа в последовательности: "))
        if a > 0:
            break
        else:
            print("Значение должно быть положительным... Повторите попытку")
    except ValueError:
        print("Неверный ввод... Повторите попытку")

print(f"Значение простого числа под номером {a}:", prime(a))
