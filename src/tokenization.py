from src.constants import DIGITS, OPERATORS


def func_tokenization(input_from_user: str) -> list[tuple[str, str]] | None:
    """
    Функция, преобразующая запись пользователя в токены (OPERATOR, NUMBER, BRACKET)
    :param input_from_user: ввод юзера
    :return: список токенов в формате: [char, ТОКЕН]
    """
    input_from_user += ' '
    before_tokenization(input_from_user)
    tokens: list[tuple[str, str]] = []
    concat: str = ''
    skip_ind: float | int = float('inf')
    for ind_symb in range(0, len(input_from_user) - 1):
        if ind_symb == skip_ind: continue
        curr_symb: str = input_from_user[ind_symb]
        if curr_symb in '()': tokens.append((curr_symb, 'BRACKET'))
        elif curr_symb in DIGITS:
            concat += curr_symb
            if not input_from_user[ind_symb + 1].isdigit() and input_from_user[ind_symb + 1] != '.':
                if concat.count('.') > 1: raise ValueError(f"{concat.count('.')} точки в одном вещественном числе")
                tokens.append((concat, 'NUMBER'))
                concat = ''
        elif curr_symb in OPERATORS:
            if curr_symb in '+-' and (not tokens or tokens[-1][0] == '(' or tokens[-1][1] == 'OPERATOR'):
                tokens.append(('〜' if curr_symb == '-' else '$', 'OPERATOR'))
            elif curr_symb + input_from_user[ind_symb+1] in '**//':
                tokens.append((curr_symb * 2, 'OPERATOR'))
                skip_ind = ind_symb + 1
            else:
                tokens.append((curr_symb, 'OPERATOR'))
    return tokens


def before_tokenization(input_from_user: str) -> None:
    """
    Функция, проверяющая корректность арифметического выражения
    :param input_from_user: ввод юзера
    :return: корректно или нет
    """
    alphabet = DIGITS + ''.join(OPERATORS) + '() '
    if input_from_user == ' ': raise ValueError("Вы ничего не ввели")
    if input_from_user.count('(') > input_from_user.count(')'): raise ValueError("Не все открывающиеся скобки закрыты")
    elif input_from_user.count('(') < input_from_user.count(')'): raise ValueError("Закрывающих скобок больше, чем открывающих")
    for ind in range(len(input_from_user) - 1):
        curr: str = input_from_user[ind]
        if curr not in alphabet: raise ValueError(f"Вы ввели недопустимые знаки! Допустимые знаки: {alphabet}")
        if curr == '(':
            closed_ind: int = input_from_user[ind:].find(')')

            if closed_ind == -1:
                raise ValueError("Неправильный порядок скобок")

            closed_ind += ind
            between: str = input_from_user[ind+1:closed_ind]

            if not len(between):
                raise ValueError("Пустые скобки")

            if between[0] in ' */%':
                raise ValueError("Некорректное выражение внутри скобок")
