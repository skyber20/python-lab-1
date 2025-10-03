from src.constants import OPERATORS, DIGITS


def before_tokenization(input_from_user: str) -> None:
    """
    Функция, проверяющая корректность арифметического выражения
    :param input_from_user: ввод юзера
    :return: корректно или нет
    """
    alphabet = DIGITS + ''.join(OPERATORS) + '() '
    if input_from_user == ' ': raise ValueError("Вы ничего не ввели")
    if input_from_user.count('(') > input_from_user.count(')'): raise Exception("Не все открывающиеся скобки закрыты")
    elif input_from_user.count('(') < input_from_user.count(')'): raise Exception("Закрывающих скобок больше, чем открывающих")
    for ind in range(len(input_from_user) - 1):
        curr = input_from_user[ind]
        if curr not in alphabet: raise ValueError(f"Вы ввели недопустимые знаки! Допустимые знаки: {alphabet}")
        if curr == '(':
            if not len(set(list(''.join(input_from_user[ind+1:input_from_user[ind+1:].find(')')+ind+1]))) & set(DIGITS)): \
                raise Exception("Неправильно набранное выражение внутри скобок")
