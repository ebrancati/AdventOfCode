import re

def extract_and_sum_multiplications(corrupted_memory):
    """
    Reads the corrupted memory from a file, extracts valid 'mul(X, Y)' instructions,
    multiplies the numbers, and returns the sum of the results.
    """

    # Regular expression to match the pattern mul(X,Y) where X and Y are integers
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches for the pattern mul(X,Y)
    matches = re.findall(pattern, corrupted_memory)
    
    total_sum = 0
    
    # For each match, multiply the numbers and add to the total sum
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y
    
    return total_sum

with open("input.txt", 'r') as file:
    corrupted_memory = file.read()

result = extract_and_sum_multiplications(corrupted_memory)
print(f"The sum of all valid multiplications is: {result}")