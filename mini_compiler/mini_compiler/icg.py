def generate_intermediate_code(ast):
    intermediate_code = []
    
    # Helper function to generate intermediate code for expressions
    def process_expr(expr):
        if expr[0] == 'number':
            return str(expr[1])  # Return the number itself
        elif expr[0] == 'id':
            return expr[1]  # Return the identifier (variable)
        elif expr[0] == 'plus':
            left = process_expr(expr[1])  # Recursively process left side of the expression
            right = process_expr(expr[2])  # Recursively process right side of the expression
            temp_var = f'temp{len(intermediate_code)}'  # Generate a temporary variable
            intermediate_code.append(f'ADD {left}, {right}, {temp_var}')  # Generate code for addition
            return temp_var  # Return the temporary variable for further operations
        elif expr[0] == 'times':
            left = process_expr(expr[1])  # Recursively process left side of the expression
            right = process_expr(expr[2])  # Recursively process right side of the expression
            temp_var = f'temp{len(intermediate_code)}'  # Generate a temporary variable
            intermediate_code.append(f'MUL {left}, {right}, {temp_var}')  # Generate code for multiplication
            return temp_var  # Return the temporary variable for further operations
        elif expr[0] == 'minus':
            left = process_expr(expr[1])  # Recursively process left side of the expression
            right = process_expr(expr[2])  # Recursively process right side of the expression
            temp_var = f'temp{len(intermediate_code)}'  # Generate a temporary variable
            intermediate_code.append(f'SUB {left}, {right}, {temp_var}')  # Generate code for subtraction
            return temp_var  # Return the temporary variable for further operations
        else:
            return None  # For unexpected cases
    
    if ast[0] == 'assign':
        left = ast[1][1]  # Variable to assign to (e.g., 'x')
        right = process_expr(ast[2])  # Process the right-hand expression
        intermediate_code.append(f'STORE {right}, {left}')  # Store the result in the variable
        
    return intermediate_code
