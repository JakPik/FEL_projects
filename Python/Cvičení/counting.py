def count_chars_in_string(string):
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts

if __name__ == "__main__":
    print(count_chars_in_string("hello"))