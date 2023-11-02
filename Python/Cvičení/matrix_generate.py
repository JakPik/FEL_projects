import random

def generate_data(n_rows, n_cols):
    return [[random.randint(0,1) for _ in range (n_cols)] for _ in range(n_rows)]

def print_data(data):
    for row in data:
        for num in row:
            print(f"{num:>3}", end = "")
        print()
    pass


if __name__ == "__main__":
    n_rows = 5
    n_cols = 5
    matrix = generate_data(n_rows, n_cols)
    print_data(matrix)