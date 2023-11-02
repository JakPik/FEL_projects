data = [[0, -1, 1],
        [-1, 0, -1],
        [1, 0, -1]]

def value_count(data, value):
    count = 0
    for row in data:
        for column in row:
            if (value == column):
                count += 1
    return count

def value_positions(data, value):
    positions = []
    for idr, row in enumerate(data):
        for idc ,column in enumerate(row):
            if (value == column):
                positions.append((idr, idc))
    return positions

if __name__ == "__main__":
    count = value_count(data, -1)
    print(count)
    positions = value_positions(data, 0)
    print(positions)
