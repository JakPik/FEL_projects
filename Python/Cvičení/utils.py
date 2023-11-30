def read_classification_from_file(filepath):
    dictonary = {}
    with open(filepath, 'rt', encoding='utf-8') as f:
        for line in f:
            string, result = line.split()
            dictonary[string] = result
    return dictonary

def write_classification_to_file(dictonary):
    with open("result.txt", 'wt', encoding="utf-8") as f:
        for letters in dictonary:
            numbers = dictonary[letters]
            string = f"{letters}  {numbers}\n"
            f.write(string)


def separate_text_and_number(string):
    n = ''.join(char for char in string if char.isdigit())
    l = ''.join(char for char in string if char.isalpha())
    numbers = ''.join(n)
    letters = ''.join(l)
    return letters, numbers

if __name__ == "__main__":
    dictonary = read_classification_from_file("./Python/Cvičení/clasification.txt")
    write_classification_to_file(dictonary)

