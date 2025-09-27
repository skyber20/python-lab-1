from tokenization import func_tokenization
from src.validation_expression import before_tokenization


def main():
    input_from_user = input("Введите арифметическое выражение: ") + ' '
    # Шаг 1 - токенизация
    before_tokenization(input_from_user)
    after_tokenization: list[tuple[str, str]] = func_tokenization(input_from_user)
    print(after_tokenization)
    # Шаг 2 - преобразование инфиксной записи в обратную польскую


if __name__ == '__main__':
    main()
