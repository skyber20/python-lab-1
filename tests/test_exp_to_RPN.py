import pytest
from src.exp_to_RPN import expression_to_RPN
from src.tokenization import func_tokenization


def test_exp_to_RPN_1():
    expr: str = '15**   (2 + 3)'
    assert expression_to_RPN(func_tokenization(expr)) == ['15', '2', '3', '+', '**']


def test_exp_to_RPN_2():
    expr: str = '2 ** 3 ** 2'
    assert expression_to_RPN(func_tokenization(expr)) == ['2', '3', '2', '**', '**']


def test_exp_to_RPN_3():
    expr: str = '100//3 %   4 * 2.34+ -5.313'
    assert expression_to_RPN(func_tokenization(expr)) == ['100', '3', '//', '4', '%', '2.34', '*', '5.313', '〜', '+']


def test_exp_to_RPN_4():
    expr: str = '((((2+3)*4)-5)*6)**2 // 10'
    assert expression_to_RPN(func_tokenization(expr)) == ['2', '3', '+', '4', '*', '5', '-', '6', '*', '2', '**', '10', '//']


def test_exp_to_RPN_5():
    expr: str = '3.5 * (2 +  - --4.53) / 2.5 - 1 + 2 ** 3'
    assert expression_to_RPN(func_tokenization(expr)) == ['3.5', '2', '4.53', '〜', '〜', '〜', '+', '*', '2.5', '/', '1', '-', '2', '3', '**', '+']


def test_exp_to_RPN_6():
    with pytest.raises(ValueError):
        expr: str = '2 + 3)'
        expression_to_RPN(func_tokenization(expr))
