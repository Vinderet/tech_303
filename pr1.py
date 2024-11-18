# Функция калькулятора
def calc(a, b, operator):
    """
    Выполняет арифметическую операцию над двумя числами

    :param a: Первое число
    :param b: Второе число
    :param operator: Оператор ('add', 'subtract', 'multiply', 'divide')
    :return возвращаем результат операции или сообщение об ошибке
    """

    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    elif operator == 'divide':
        if b == 0:
            return 'Деление на ноль невозможно'
        return a / b
    else:
        return "Неверный оператор"


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

    print("Сложение:", calc(num1, num2, "add"))
    print("Вычитание:", calc(num1, num2, 'subtract'))
    print("Умножение:", calc(num1, num2, 'multiply'))
    print("Деление:", calc(num1, num2, 'divide'))
    print("Объединение строк:", concatenate_strings(str1, str2))
    print("Повторение строки:", repeat_string(str1, n))


def test_calc():
    assert calc(5, 10, 'add') == 15


# Вызов тестов
test_calc()
print('Тесты успешно пройдены!')

# Вызов основной функции
main()
