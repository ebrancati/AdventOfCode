def is_safe_report(report):
    """
    Checks if a report is safe based on the following rules:
    - The sequence of numbers is either strictly increasing or strictly decreasing.
    - The difference between consecutive numbers is at least 1 and at most 3.
    """
    # Check if the levels are either strictly increasing or strictly decreasing
    is_increasing = True
    is_decreasing = True
    
    # Check the differences between adjacent levels
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        
        # If the difference is outside the valid range, the report is unsafe
        if diff < 1 or diff > 3:
            return False
        
        # Determine if the report is increasing or decreasing
        if report[i] > report[i - 1]:
            is_decreasing = False
        elif report[i] < report[i - 1]:
            is_increasing = False
    
    # The report is safe if it's either increasing or decreasing
    return is_increasing or is_decreasing

def count_safe_reports(reports):
    """
    Counts how many reports are safe
    """
    safe_count = 0
    
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    
    return safe_count

def get_data(filename):
    """
    Reads the input data from a file and returns a list of reports.
    Each report is a list of integers.
    """
    reports = []
    with open(filename, 'r') as file:
        for line in file:
            # Convert each line of space-separated numbers to a list of integers
            reports.append(list(map(int, line.split())))
        
    return reports

filename = 'input.txt'
reports = get_data(filename)

safe_reports = count_safe_reports(reports)

print(f"Number of safe reports: {safe_reports}")