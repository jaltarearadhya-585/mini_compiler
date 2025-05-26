def parse_input(tokens):
    tokens = iter(tokens)
    return parse_expression(tokens)

def parse_expression(tokens):
    left = parse_term(tokens)
    while True:
        token = next(tokens, None)
        if token and token[0] == 'PLUS':
            right = parse_term(tokens)
            left = ('plus', left, right)
        else:
            break
    return left

def parse_term(tokens):
    left = parse_factor(tokens)
    while True:
        token = next(tokens, None)
        if token and token[0] == 'TIMES':
            right = parse_factor(tokens)
            left = ('times', left, right)
        else:
            break
    return left

def parse_factor(tokens):
    token = next(tokens, None)
    if token[0] == 'NUMBER':
        return ('number', int(token[1]))
    elif token[0] == 'ID':
        return ('id', token[1])
    elif token[0] == 'LPAREN':
        expr = parse_expression(tokens)
        if next(tokens)[0] != 'RPAREN':
            raise SyntaxError('Expected closing parenthesis')
        return expr
    else:
        raise SyntaxError('Unexpected token: {}'.format(token))
