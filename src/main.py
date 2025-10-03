from tokenization import func_tokenization
from src.validation_expression import before_tokenization
from src.exp_to_RPN import expression_to_RPN
from src.exp_calculate import func_calculate


def main() -> None:
    """
    Точка входа. Принтует результат каждой отдельной функции
    :return: None
    """
    input_from_user: str = input("Введите арифметическое выражение: ")
    # Шаг 1 - токенизация
    after_tokenization: list[tuple[str, str]] = func_tokenization(input_from_user)
    print(f"После токенизации: {after_tokenization}")
    # Шаг 2 - преобразование инфиксной записи в обратную польскую
    convert_to_rpn: list[str] = expression_to_RPN(after_tokenization)
    print(f"После преобразования в RPN: {convert_to_rpn}")
    # Шаг 3 - вычисление выражение в обратной польской
    res: str = func_calculate(convert_to_rpn)
    print(f"Результат: {res}")


if __name__ == '__main__':
    main()
