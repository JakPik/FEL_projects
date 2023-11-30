def count_rows_and_words(filepath):
    with open(filepath, 'rt', encoding="utf=8") as f:
        count_rows = 0
        count_words = 0
        for string in f:
            count_rows += 1
            words = []
            words = string.split()
            for i in words:
                count_words += 1
    touple = (count_rows, count_words)
    return touple


if __name__ == "__main__":
    count_rows_and_words("./Python/Cvičení/example.txt")