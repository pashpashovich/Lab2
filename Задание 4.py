import math


def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError("Отрицательное число не имеет квадратного корня")
        result = math.sqrt(number)
        return result
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
    finally:
        print("Завершение операции")


try:
    num = float(input("Введите число для вычисления квадратного корня: "))
    result = calculate_square_root(num)
    if result is not None:
        print(f"Квадратный корень: {result:.2f}")
except KeyboardInterrupt:
    print("\nПрограмма завершена пользователем")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Завершение программы")
