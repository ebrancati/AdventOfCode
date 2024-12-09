import re

def extract_and_sum_multiplications(memory):
    """
    Reads the corrupted memory from a file, extracts valid 'mul(X, Y)' instructions,
    multiplies the numbers, and returns the sum of the results.
    """
    mul_enabled = True 
    total_sum = 0

    tokens = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', memory)

    for token in tokens:
        if token.startswith("mul"):
            # Extract numbers and calculate product
            if mul_enabled:
                nums = list(map(int, re.findall(r'\d+', token)))
                total_sum += nums[0] * nums[1]
        elif token == "do()":
            mul_enabled = True  # Enable future mul instructions
        elif token == "don't()":
            mul_enabled = False  # Disable future mul instructions

    return total_sum

with open('input.txt', 'r') as file:
    memory_string = file.read().strip()

result = extract_and_sum_multiplications(memory_string)
print(f"The sum of all valid multiplications is: {result}")
