from icg import generate_icg

input_code = "x = 5 + 3 * (2 - 1)"

icg_output = generate_icg(input_code)
print("Intermediate Code:")
for line in icg_output:
    print(line)
