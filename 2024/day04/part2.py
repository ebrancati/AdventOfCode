with open("input.txt", "r") as file:
    grid = [line.strip() for line in file]

nRows, nCols = len(grid), len(grid[0])

totalCombs = 0

for i in range(1, nRows - 1):
    for j in range(1, nCols - 1):
        if grid[i][j] == "A":
            top_left = grid[i-1][j-1]
            bottom_right = grid[i+1][j+1]
            bottom_left = grid[i+1][j-1]
            top_right = grid[i-1][j+1]

            if ((top_left == "M" and bottom_right == "S") or 
                (top_left == "S" and bottom_right == "M")) and \
               ((bottom_left == "M" and top_right == "S") or 
                (bottom_left == "S" and top_right == "M")):
                totalCombs += 1

print(totalCombs)
