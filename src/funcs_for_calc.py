from src.Errors_classes import CalculateError

def float_or_int(n: float | int | str) -> float | int:
    """
    Проверка, целочисленное или число с плавающей запятой
    :param n: число
    :return: флоат, если число с плавающей запятой. инт, если нет
    """
    n = str(float(n))
    return int(n[:n.find('.')]) if len(n[n.find('.')+1:]) == 1 and n[n.find('.')+1] == '0' else float(n)


def add(a: int | float, b: int | float) -> int | float:
    """
    функция, складывающая 2 числа
    :param a: число 1
    :param b: число 2
    :return: сумма 2ух чисел
    """
    return a + b


def diff(a: int | float, b: int | float) -> int | float:
    """
    функция, вычитающая 2 числа
    :param a: число 1
    :param b: число 2
    :return: разность 2ух чисел
    """
    return a - b


def multy(a: int | float, b: int | float) -> int | float:
    """
    функция, умножающая 2 числа
    :param a: число 1
    :param b: число 2
    :return: произведение 2ух чисел
    """
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """
    функция, делящая число a на b
    :param a: число 1
    :param b: число 2
    :return: Частное 2ух чисел, если b != 0, иначе ошибка
    """
    if b == 0:
        raise ZeroDivisionError("Деление на 0")
    return float_or_int(a / b)


def power(a: int | float, b: int | float) -> int | float:
    """
    :param a: число 1
    :param b: число 2
    :return: результат возведения числа a в степень b
    """
    return a ** b


def integer_division(a: int | float, b: int | float) -> int:
    """
    функция, делящаяя 2 ЦЕЛОЧИСЛЕННЫХ числа
    :param a: число 1
    :param b: число 2
    :return: целочисленное деление 2ух чисел, если b != 0, иначе ошибка
    """
    if b == 0:
        raise ZeroDivisionError("Деление на 0")
    if '.' in str(a) or '.' in str(b):
        raise CalculateError("Невозможно выполнить целочисленное деление, если 2 числа не целые")
    return int(a // b)


def mod(a: int | float, b: int | float):
    """
    :param a: число 1
    :param b: число 2
    :return: остаток от числа a при делении на число b != 0, иначе ошибка
    """
    if b == 0:
        raise ZeroDivisionError("Деление на 0")
    if '.' in str(a) or '.' in str(b):
        raise CalculateError("Невозможно выполнить деление с остатком, если 2 числа не целые")
    return a % b


def unar_plus(a: int | float) -> int | float:
    """
    :param a: число
    :return: a
    """
    return a


def unar_minus(a: int | float) -> int | float:
    """
    :param a: число
    :return: -a
    """
    return -a
