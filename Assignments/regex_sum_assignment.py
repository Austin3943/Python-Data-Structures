import re

# Define the file name
file_name = 'regex_sum_42.txt'

# Try to open and read the file
try:
    with open(file_name, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    quit()

# Extract numbers using regex
numbers = [int(num) for num in re.findall(r'[0-9]+', text)]

# Debugging: Print the count of numbers and the numbers themselves
print(f"Found {len(numbers)} numbers: {numbers}")

# Compute and print the sum
sum_result = sum(numbers)
print(f"Sum: {sum_result}")
