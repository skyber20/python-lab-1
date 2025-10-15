from src.constants import PRIORITETS
from src.class_Stack import Stack
from src.Errors_classes import BracketsError


def expression_to_RPN(tokens: list[tuple[str, str]]) -> list[str]:
    """
    Функция, преобразующая токены в обратную польскую запись.
    Алгоритм:
    Если встретилось число -> аппендим в аутпут.
    Если встретился оператор, сравниваем с операторами в стеке операторов.
        Если текущий оператор имеет приоритет выше, чем самый верхний оператор в стеке, то пушим текущий оператор в стек.
        Если текущий приоритет равен или меньше верхнего из стека, то верхний оператор стека вынимаем и аппендим в аутпут, а
        текущий пушим в стек.
        Так до тех пор, пока не встретим в стеке операторов открывающуюся скобку, или пока не дойдем до конца стека,
        или пока не найдем оператор, чем приоритет выше текущего.
    Если встретилась открывающаяся скобка -> пушим в стек операторов
    Если встретилась закрывающая скобка, то начинаем из стека вынимать верхние элементы и аппендить их в аутпут.
    Так до тех пор, пока не встретим открывающуюся скобку (её потом удаляем из стека операторов).
    :param tokens: список токенов в формате: [char, ТОКЕН]
    :return: выражение, записанное в RPN
    """
    output: list[str] = []
    stack_operators: Stack = Stack()

    for token in tokens:
        if token[-1] == 'NUMBER':
            output.append(token[0])
        elif token[0] == '(':
            stack_operators.push(token[0])
        elif token[0] == '**' and (stack_operators.is_empty() or stack_operators.top() == '**'):
            stack_operators.push('**')
        elif token[-1] == 'OPERATOR' and token[0] not in '()':
            while not stack_operators.is_empty():
                operator: str = stack_operators.top()
                if operator == '(' or PRIORITETS[operator] < PRIORITETS[token[0]] or \
                        (token[0] in '〜$' and stack_operators.top() in '〜$'):
                    break
                else:
                    output.append(operator)
                    stack_operators.pop()
            stack_operators.push(token[0])
        elif token[0] == ')':
            find_open_bracket: bool = False
            while not stack_operators.is_empty() and not find_open_bracket:
                operator1: str = stack_operators.top()
                if operator1 == '(':
                    find_open_bracket = True
                else:
                    output.append(operator1)
                stack_operators.pop()
            if not find_open_bracket:
                raise BracketsError("Закрывающих скобок больше, чем открывающих")
    while not stack_operators.is_empty():
        operator2: str = stack_operators.top()
        if operator2 == '(':
            raise BracketsError("Открывающих скобок больше, чем закрывающих")
        output.append(operator2)
        stack_operators.pop()
    return output
