import pytest
from src.exp_calculate import func_calculate


def test_exp_calc_1():
    expr: list[str] = ['2', '3', '+']
    assert func_calculate(expr) == '5'


def test_exp_calc_2():
    expr: list[str] = ['4', '2', '3', '+', '**']
    assert func_calculate(expr) == '1024'


def test_exp_calc_3():
    expr: list[str] = ['100', '3', '//', '4', '%', '2.34', '*', '5.313', '〜', '+']
    assert func_calculate(expr) == '-2.973'


def test_exp_calc_4():
    expr: list[str] = ['2', '3', '+', '4', '*', '5', '-', '6', '*', '2', '**', '10', '//']
    assert func_calculate(expr) == '810'


def test_exp_calc_5():
    expr: list[str] = ['3.5', '2', '4.53', '〜', '〜', '〜', '+', '*', '2.5', '/', '1', '-', '2', '3', '**', '+']
    assert func_calculate(expr) == '3.458'


def test_exp_calc_6():
    with pytest.raises(Exception):
        expr: list[str] = ['3', '4', '2', '-']
        assert func_calculate(expr)


def test_exp_calc_7():
    with pytest.raises(Exception):
        expr: list[str] = ['3', '4', '2', '-']
        assert func_calculate(expr)


def test_exp_calc_8():
    with pytest.raises(Exception):
        expr: list[str] = ['8.0', '4', '//']
        assert func_calculate(expr)


def test_exp_calc_9():
    with pytest.raises(Exception):
        expr: list[str] = ['13', '4.0', '//']
        assert func_calculate(expr)


def test_exp_calc_10():
    with pytest.raises(Exception):
        expr: list[str] = ['3', '0', '/']
        assert func_calculate(expr)
