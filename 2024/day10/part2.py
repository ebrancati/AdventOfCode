def count_distinct_trails(topographic_map):
    rows, cols = len(topographic_map), len(topographic_map[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, current_height):
        if topographic_map[x][y] == 9:
            return 1
        trails = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and topographic_map[nx][ny] == current_height + 1:
                trails += dfs(nx, ny, current_height + 1)
        return trails

    total_rating = 0
    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:
                total_rating += dfs(i, j, 0)
    return total_rating

topographic_map = ""

with open("input.txt", 'r') as file:
    topographic_map = [list(map(int, line.strip())) for line in file]

total_rating = count_distinct_trails(topographic_map)
print(total_rating)
