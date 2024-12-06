from collections import Counter

def get_data(filename):
    left_list = []
    right_list = []

    # Read the file and process each line
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two values and convert them to integers
            left_value, right_value = map(int, line.split())

            left_list.append(left_value)
            right_list.append(right_value)
    
    return left_list, right_list

def calculate_similarity(left_list, right_list):

    # Count occurrences of each number in the right list
    right_count = Counter(right_list)
    
    similarity_score = 0
    
    # For each number in the left list, multiply by the count from the right list
    for num in left_list:
        similarity_score += num * right_count[num]
    
    return similarity_score

filename = "input.txt"

left_list, right_list = get_data(filename)

left_list.sort()
right_list.sort()

# Calculate and print the similarity score
similarity_score = calculate_similarity(left_list, right_list)
print(f"The similarity score is: {similarity_score}")