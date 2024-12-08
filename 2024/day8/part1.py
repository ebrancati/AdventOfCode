def read_input(file_name):

    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_antennas(map_data):

    antennas = []
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas

def calculate_antinodes(antennas, width, height):

    antinode_positions = set()

    freq_groups = {}
    for x, y, freq in antennas:
        if freq not in freq_groups:
            freq_groups[freq] = []
        freq_groups[freq].append((x, y))

    for freq, locations in freq_groups.items():
        n = len(locations)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                dx = x2 - x1
                dy = y2 - y1

                ax1 = x1 - dx
                ay1 = y1 - dy
                ax2 = x2 + dx
                ay2 = y2 + dy

                if 0 <= ax1 < width and 0 <= ay1 < height:
                    antinode_positions.add((ax1, ay1))
                if 0 <= ax2 < width and 0 <= ay2 < height:
                    antinode_positions.add((ax2, ay2))

    return antinode_positions

def main():

    map_data = read_input('input.txt')
    width = len(map_data[0])
    height = len(map_data)

    antennas = find_antennas(map_data)

    antinode_positions = calculate_antinodes(antennas, width, height)

    print("N :", len(antinode_positions))

if __name__ == "__main__":
    main()