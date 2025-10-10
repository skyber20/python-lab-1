from typing import Callable
from src.funcs_for_calc import (
    add, diff, multy, divide, integer_division, mod, power, unar_minus, unar_plus
)

OPERATORS: list[str] = ['+', '-', '*', '/', '//', '%', '**', '〜', '$']
DIGITS = '0123456789.'
PRIORITETS: dict[str, int] = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '//': 2,
    '%': 2,
    '**': 3,
    '〜': 4,
    '$': 4
}
OPERATOR_FUNCS: dict[str, Callable] = {
    '+': add,
    '-': diff,
    '*': multy,
    '/': divide,
    '//': integer_division,
    '%': mod,
    '**': power,
    '〜': unar_minus,
    '$': unar_plus
}
