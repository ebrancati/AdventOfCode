def get_data(filename):
    """
    Reads data from a file and returns two lists: 
    one for the left values and one for the right values.
    """
    
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

filename = "input.txt"

left_list, right_list = get_data(filename)

left_list.sort()
right_list.sort()

# Pairs the elements of the two lists (zip) 
# calculates the absolute difference between the corresponding elements (abs)
# adds all the absolute differences to obtain the total distance.(sum)
total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))

print(f"The total distance is: {total_distance}")
