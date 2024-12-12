def count_xmas_in_grid(grid):
    def check_direction(x, y, dx, dy):
        word = "XMAS"
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return 0
        return 1

    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Diagonal Down-Right
        (1, -1), # Diagonal Down-Left
        (0, -1), # Left
        (-1, 0), # Up
        (-1, -1),# Diagonal Up-Left
        (-1, 1)  # Diagonal Up-Right
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                count += check_direction(x, y, dx, dy)

    return count

with open("input.txt", "r") as file:
    grid = [line.strip() for line in file]

# Conta le occorrenze di "XMAS" nella griglia
result = count_xmas_in_grid(grid)
print(result)