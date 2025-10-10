import pytest
from src.tokenization import func_tokenization


def test_token_expr_1():
    expr: str = '15**   (2 + 3)'
    assert func_tokenization(expr) == [('15', 'NUMBER'), ('**', 'OPERATOR'), ('(', 'BRACKET'), ('2', 'NUMBER'), \
                                       ('+', 'OPERATOR'), ('3', 'NUMBER'), (')', 'BRACKET')]


def test_token_expr_2():
    expr: str = '2 ** 3 ** --2'
    assert func_tokenization(expr) == [('2', 'NUMBER'), ('**', 'OPERATOR'), ('3', 'NUMBER'), ('**', 'OPERATOR'), \
                                       ('〜', 'OPERATOR'), ('〜', 'OPERATOR'), ('2', 'NUMBER')]


def test_token_expr_3():
    expr: str = '100//3 %   4 * 2.34+ -5.313'
    assert func_tokenization(expr) == [('100', 'NUMBER'), ('//', 'OPERATOR'), ('3', 'NUMBER'), ('%', 'OPERATOR'), \
                                       ('4', 'NUMBER'), ('*', 'OPERATOR'), ('2.34', 'NUMBER'), ('+', 'OPERATOR'), \
                                       ('〜', 'OPERATOR'), ('5.313', 'NUMBER')]


def test_token_expr_4():
    expr: str = '((((2+3)*4)-5)*6)**2 // 10'
    assert func_tokenization(expr) == [('(', 'BRACKET'), ('(', 'BRACKET'), ('(', 'BRACKET'), ('(', 'BRACKET'), \
                                       ('2', 'NUMBER'), ('+', 'OPERATOR'), ('3', 'NUMBER'), (')', 'BRACKET'), \
                                       ('*', 'OPERATOR'), ('4', 'NUMBER'), (')', 'BRACKET'), ('-', 'OPERATOR'), \
                                       ('5', 'NUMBER'), (')', 'BRACKET'), ('*', 'OPERATOR'), ('6', 'NUMBER'), \
                                       (')', 'BRACKET'), ('**', 'OPERATOR'), ('2', 'NUMBER'), ('//', 'OPERATOR'), ('10', 'NUMBER')]


def test_token_expr_5():
    expr: str = '3.5 * (2 +  - --4.53) / 2.5 - 1 + 2 ** 3'
    assert func_tokenization(expr) == [('3.5', 'NUMBER'), ('*', 'OPERATOR'), ('(', 'BRACKET'), ('2', 'NUMBER'), \
                                       ('+', 'OPERATOR'), ('〜', 'OPERATOR'), ('〜', 'OPERATOR'), ('〜', 'OPERATOR'), \
                                       ('4.53', 'NUMBER'), (')', 'BRACKET'), ('/', 'OPERATOR'), ('2.5', 'NUMBER'), \
                                       ('-', 'OPERATOR'), ('1', 'NUMBER'), ('+', 'OPERATOR'), ('2', 'NUMBER'), \
                                       ('**', 'OPERATOR'), ('3', 'NUMBER')]


def test_token_expr_6():
    with pytest.raises(ValueError):
        expr: str = '1 + 1.2 + 1.2.3'
        func_tokenization(expr)


def test_token_expr_7():
    with pytest.raises(ValueError):
        expr: str = ''
        func_tokenization(expr)


def test_token_expr_8():
    with pytest.raises(ValueError):
        expr: str = '2 + (45 - 6'
        func_tokenization(expr)


def test_token_expr_9():
    with pytest.raises(ValueError):
        expr: str = '19 - 23 + 6)'
        func_tokenization(expr)


def test_token_expr_10():
    with pytest.raises(ValueError):
        expr: str = '2 ! 3 - 4'
        func_tokenization(expr)


def test_token_expr_11():
    with pytest.raises(ValueError):
        expr: str = '2 + ()'
        func_tokenization(expr)


def test_token_expr_12():
    with pytest.raises(ValueError):
        expr: str = ')4 + 3 ('
        func_tokenization(expr)


def test_token_expr_13():
    with pytest.raises(ValueError):
        expr = '2 + (* 3 - 4)'
        func_tokenization(expr)
