# TODO: 1) Провести рефакторинг кода 2) Оптимизация 3) Документация 4) Тестирование

# Исходный код

# Функция для сложения двух чисел
def add_numbers(a, b):
    return a + b


# Функция для вычитания двух чисел
def subtract_numbers(a, b):
    return a - b


# Функция для умножения двух чисел
def multiply_numbers(a, b):
    return a * b


# Функция для деления двух чисел
def divide_numbers(a, b):
    return a / b


# Функция для объединения двух строк
def concatenate_strings(str1, str2):
    return str1 + str2


# Функция для повторения строки n раз
def repeat_string(str1, n):
    return str1 * n


# Основная функция
def main():
    num1 = 10
    num2 = 5
    str1 = "Hello"
    str2 = "World"
    n = 3

    print("Сложение:", add_numbers(num1, num2))
    print("Вычитание:", subtract_numbers(num1, num2))
    print("Умножение:", multiply_numbers(num1, num2))
    print("Деление:", divide_numbers(num1, num2))
    print("Объединение строк:", concatenate_strings(str1, str2))
    print("Повторение строки:", repeat_string(str1, n))


# Вызов основной функции
main()
