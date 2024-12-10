def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads_and_scores(topographic_map):
    rows, cols = len(topographic_map), len(topographic_map[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y, current_height):
        if topographic_map[x][y] == 9:
            return {(x, y)}
        reachable_nines = set()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and topographic_map[nx][ny] == current_height + 1:
                reachable_nines |= dfs(nx, ny, current_height + 1)
        return reachable_nines

    scores = []
    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:
                reachable = dfs(i, j, 0)
                scores.append(len(reachable))
    return sum(scores)

if __name__ == "__main__":
    topographic_map = read_map("input.txt")
    total_score = find_trailheads_and_scores(topographic_map)
    print(total_score)