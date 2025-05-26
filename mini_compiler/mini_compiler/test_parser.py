from parser import parse_input

input_code = "x = 5 + 3 * (2 - 1)"

parsed_tree = parse_input(input_code)
print("Parsed Tree:", parsed_tree)
