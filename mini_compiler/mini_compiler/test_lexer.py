from lexer import lexer

input_code = "x = 5 + 3 * (2 - 1)"

lexer.input(input_code)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
