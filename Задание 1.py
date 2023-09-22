def prime(num):
    i = 0
    current = 2
    while i < num:
        k = 0
        for t in range(2, current):
            if current % t == 0:
                k = k + 1
                break  # Add this line to exit the loop if a divisor is found
        if k == 0:
            i = i + 1
        current = current + 1  # Move this line outside the for loop
    return current - 1  # Subtract 1 to return the correct prime number


while True:
    try:
        a = int(input("Введите номер простого числа в последовательности: "))
        if a > 0:
            break
        else:
            print("Значение должно быть положительным... Повторите попытку")
    except ValueError:
        print("Неверный ввод... Повторите попытку")

print(f"Значение простого числа под номером {a}:", prime(a))
