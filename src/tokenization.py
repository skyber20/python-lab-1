from src.constants import DIGITS, OPERATORS


def func_tokenization(input_from_user: str) -> list[tuple[str, str]] | None:
    tokens: list[tuple[str, str]] = []
    concat: str = ''
    skip_ind: float | int = float('inf')
    for ind_symb in range(0, len(input_from_user) - 1):
        if ind_symb == skip_ind: continue
        curr_symb: str = input_from_user[ind_symb]
        if curr_symb in '()': tokens.append((curr_symb, 'BRACKET'))
        elif curr_symb in DIGITS:
            concat += curr_symb
            if not input_from_user[ind_symb + 1].isdigit() and input_from_user[ind_symb + 1] != '.':
                if concat.count('.') > 1: raise ValueError(f"{concat.count('.')} точки в одном вещественном числе")
                tokens.append((concat, 'NUMBER'))
                concat = ''
        elif curr_symb in OPERATORS:
            if curr_symb in '+-' and (not tokens or tokens[-1][0] == '(' or tokens[-1][1] == 'OPERATOR'):
                tokens.append(('〜' if curr_symb == '-' else '$', 'OPERATOR'))
            elif curr_symb + input_from_user[ind_symb+1] in '**//':
                tokens.append((curr_symb * 2, 'OPERATOR'))
                skip_ind = ind_symb + 1
            else:
                tokens.append((curr_symb, 'OPERATOR'))
    return tokens
