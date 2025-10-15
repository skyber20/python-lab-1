from src.class_Stack import Stack
from src.constants import OPERATORS, OPERATOR_FUNCS
from src.Errors_classes import FatalError, OpersMoreNumsError


def func_calculate(exp_in_rpn: list[str]) -> str:
    """
    считает значение выражения в RPN при помощи стека чисел. если встретился унарный оператор,
    то берет последнее запушенное в Стек число и выполняет над ним операцию. другие же операторы требуют два операнда.
    Выполняет действие и результат пушится в Стек чисел снова. если выражение корректно, то в конечном итоге в стеке должно
    остаться единственное значение. Это и есть ответ
    :param exp_in_rpn: упорядоченный (учитывающий приоритеты) список операндов и операторов. выполнять действия над
    списком необходимо последовательно
    :return: если в стеке по итогу 1 число - это наш результат. если стек пустой или больше 1 элемента, то ошибка
    """
    stack_nums: Stack = Stack()
    for elem in exp_in_rpn:
        if elem not in OPERATORS:
            stack_nums.push(elem)
        else:
            if elem in '〜$':
                if stack_nums.length():
                    num: int | float = int(stack_nums.pop()) if '.' not in stack_nums.top() else float(stack_nums.pop())
                    res: int | float = OPERATOR_FUNCS[elem](num)
                    stack_nums.push(str(res))
                else:
                    raise OpersMoreNumsError(f"В стеке не нашлось числа для выполнения операции {elem}")
            else:
                if stack_nums.length() > 1:
                    num2: int | float = int(stack_nums.pop()) if '.' not in stack_nums.top() else float(stack_nums.pop())
                    num1: int | float = int(stack_nums.pop()) if '.' not in stack_nums.top() else float(stack_nums.pop())
                    res1: int | float = OPERATOR_FUNCS[elem](num1, num2)
                    stack_nums.push(str(res1))
                else:
                    raise OpersMoreNumsError(f"В стеке не нашлось 2ух чисел для выполнения операции {elem}")
    if stack_nums.length() == 1:
        return stack_nums.pop()
    raise FatalError("Не получилось вычислить выражение")
