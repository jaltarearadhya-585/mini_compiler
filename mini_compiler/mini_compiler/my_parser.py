def parse(tokens):
    if len(tokens) == 5 and tokens[1][0] == 'ASSIGN':
        return ('assign', tokens[0][1], ('binop', tokens[2][1], tokens[3][1], tokens[4][1]))
    return ('error',)