from tokenization import func_tokenization
from src.validation_expression import before_tokenization
from src.exp_to_RPN import set_prioritets
from src.exp_calculate import func_calculate


def main() -> None:
    input_from_user: str = input("Введите арифметическое выражение: ") + ' '
    # Шаг 1 - токенизация
    before_tokenization(input_from_user)
    after_tokenization: list[tuple[str, str]] = func_tokenization(input_from_user)
    print(after_tokenization)
    # Шаг 2 - преобразование инфиксной записи в обратную польскую
    convert_to_rpn = set_prioritets(after_tokenization)
    print(convert_to_rpn)
    res = func_calculate(convert_to_rpn)
    print(res)


# def main():
#     # inp = input()
#     print(func_calculate(['2', '10', '*', '4', '2', '**', '3', '**', '+']))

if __name__ == '__main__':
    main()
