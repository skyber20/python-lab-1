from src.class_Stack import Stack
from src.constants import OPERATORS, OPERATOR_FUNCS


def func_calculate(exp_in_rpn: list[str]) -> str:
    stack_nums: Stack = Stack()
    for elem in exp_in_rpn:
        if elem not in OPERATORS:
            stack_nums.push(elem)
        else:
            if elem in '〜$':
                try:
                    num: int | float = int(stack_nums.pop()) if '.' not in stack_nums.top() else float(stack_nums.pop())
                    res: int | float = OPERATOR_FUNCS[elem](num)
                    stack_nums.push(str(res))
                except Exception:
                    raise Exception(f"В стеке не нашлось числа для выполнения операции {elem}")
            else:
                try:
                    num2: int | float = int(stack_nums.pop()) if '.' not in stack_nums.top() else float(stack_nums.pop())
                    num1: int | float = int(stack_nums.pop()) if '.' not in stack_nums.top() else float(stack_nums.pop())
                    res: int | float = OPERATOR_FUNCS[elem](num1, num2)
                    stack_nums.push(str(res))
                except Exception:
                    raise Exception(f"В стеке не нашлось 2ух чисел для выполнения операции {elem}")
    if stack_nums.length() == 1:
        return stack_nums.pop()
    raise ArithmeticError("Не получилось вычислить выражение")
