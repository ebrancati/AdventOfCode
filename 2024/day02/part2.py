def is_safe_report(report):
    """
    Checks if a report is safe based on the following rules:
    - The sequence of numbers is either strictly increasing or strictly decreasing.
    - The difference between consecutive numbers is at least 1 and at most 3.
    """
    is_increasing = True
    is_decreasing = True
    
    # Check the differences between adjacent levels
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        
        # If the difference is outside the range [1, 3], the report is unsafe
        if diff < 1 or diff > 3:
            return False
        
        # Check if the sequence is increasing or decreasing
        if report[i] > report[i - 1]:
            is_decreasing = False
        elif report[i] < report[i - 1]:
            is_increasing = False

    # The report is safe if it is either strictly increasing or strictly decreasing
    return is_increasing or is_decreasing


def is_safe_report_with_one_removal(report):
    """
    Checks if a report is safe by considering the removal of a single level.
    - If the report is already safe, return True.
    - Otherwise, remove one level at a time and check if the report becomes safe.
    """
    # If the report is already safe, no need to remove anything
    if is_safe_report(report):
        return True

    # Try removing each level one at a time and check if the report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Create a new report by removing level i
        if is_safe_report(modified_report):
            return True  # If removing a level makes it safe, return True
    
    # If no removal makes the report safe, return False
    return False


def count_safe_reports(reports):
    """
    Counts how many reports are safe, considering the possibility of removing one level.
    """
    safe_count = 0
    for report in reports:
        if is_safe_report_with_one_removal(report):
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
            # Read each line, split it into numbers, and add it to the reports list
            reports.append(list(map(int, line.split())))
    return reports


filename = 'input.txt'
reports = get_data(filename)
safe_reports = count_safe_reports(reports)

print(f"Number of safe reports (considering removal of one level): {safe_reports}")