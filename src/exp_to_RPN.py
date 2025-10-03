from src.constants import PRIORITETS
from src.class_Stack import Stack


def expression_to_RPN(tokens: list[tuple[str, str]]) -> list[str]:
    output: list[str] = []
    stack_operators: Stack = Stack()

    for token in tokens:
        if token[-1] == 'NUMBER':
            output.append(token[0])
        elif token[0] == '(': stack_operators.push(token[0])
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
                operator: str = stack_operators.top()
                if operator == '(':
                    find_open_bracket = True
                else:
                    output.append(operator)
                stack_operators.pop()
            if not find_open_bracket: raise ValueError("Закрывающих скобок больше, чем открывающих")
    while not stack_operators.is_empty():
        operator: str = stack_operators.top()
        if operator == '(': raise ValueError("Открывающих скобок больше, чем закрывающих")
        output.append(operator)
        stack_operators.pop()
    return output
