def float_or_int(n: float | int| str) -> float | int:
    n = str(float(n))
    return int(n[:n.find('.')]) if len(n[n.find('.')+1:]) == 1 and n[n.find('.')+1] == '0' else float(n)


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def diff(a: int | float, b: int | float) -> int | float:
    return a - b


def multy(a: int | float, b: int | float) -> int | float:
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    if b == 0: raise ZeroDivisionError("Деление на 0")
    return float_or_int(a / b)


def pow(a: int | float, b: int | float) -> int | float:
    return a ** b


def integer_division(a: int | float, b: int | float) -> int:
    if b == 0: raise ZeroDivisionError("Деление на 0")
    if '.' in str(a) or '.' in str(b):
        raise Exception("Невозможно выполнить целочисленное деление, если 2 числа не целые")
    return int(a // b)


def mod(a: int | float, b: int | float):
    if b == 0: raise ZeroDivisionError("Деление на 0")
    if '.' in str(a) or '.' in str(b):
        raise Exception("Невозможно выполнить деление с остатком, если 2 числа не целые")
    return a % b


def unar_plus(a: int | float) -> int | float:
    return a


def unar_minus(a: int | float) -> int | float:
    return -a
