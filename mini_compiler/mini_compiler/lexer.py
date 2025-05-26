import re

def lexer(input_code):
    tokens = []
    token_specification = [
        ('NUMBER', r'\d+'),   # Integer number
        ('PLUS', r'\+'),      # Addition
        ('MINUS', r'-'),      # Subtraction
        ('TIMES', r'\*'),     # Multiplication
        ('DIVIDE', r'/'),     # Division
        ('ID', r'[A-Za-z]+'), # Identifiers (variables)
        ('ASSIGN', r'='),     # Assignment
        ('LPAREN', r'\('),    # Left Parenthesis
        ('RPAREN', r'\)'),    # Right Parenthesis
        ('SKIP', r'[ \t\n]+'), # Skip spaces and tabs
        ('MISMATCH', r'.'),   # Any other character (error handling)
    ]
    
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    
    for mo in re.finditer(tok_regex, input_code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        elif kind:
            tokens.append((kind, value))
    
    return tokens
