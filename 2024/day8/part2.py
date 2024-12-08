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

    from math import gcd

    antinode_positions = set()

    freq_groups = {}
    for x, y, freq in antennas:
        if freq not in freq_groups:
            freq_groups[freq] = []
        freq_groups[freq].append((x, y))

    for freq, locations in freq_groups.items():
        n = len(locations)
        if n < 2:
            continue

        for loc in locations:
            antinode_positions.add(loc)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                dx = x2 - x1
                dy = y2 - y1
                step_gcd = gcd(dx, dy)
                step_x = dx // step_gcd
                step_y = dy // step_gcd

                nx, ny = x1, y1
                while 0 <= nx < width and 0 <= ny < height:
                    antinode_positions.add((nx, ny))
                    nx -= step_x
                    ny -= step_y

                nx, ny = x2, y2
                while 0 <= nx < width and 0 <= ny < height:
                    antinode_positions.add((nx, ny))
                    nx += step_x
                    ny += step_y

    return antinode_positions

def main():

    map_data = read_input('input.txt')
    width = len(map_data[0])
    height = len(map_data)

    antennas = find_antennas(map_data)

    antinode_positions = calculate_antinodes(antennas, width, height)

    print("N: ", len(antinode_positions))

if __name__ == "__main__":
    main()
