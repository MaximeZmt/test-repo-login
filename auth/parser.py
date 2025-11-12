from auth.api import API


def evaluate_expression(memory, expr: str) -> (str, bool):
    token = expr.split()

    if len(token) < 1:
        raise ValueError("Invalid expression")

    if token[0] not in API:
        raise ValueError("Invalid command")

    return API[token[0]](memory, *token[1:])
