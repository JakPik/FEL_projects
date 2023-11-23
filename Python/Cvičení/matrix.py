class MyMatrix:

    def __init__(self, matrix=None):
        if(matrix == None):
            self.matrix = []
        else:
            self.matrix = matrix
        self.f = None

    def print_matrix(self):
        for idx, i in enumerate(self.matrix):
            print(i)

    def save(self, filename):
        f = open(filename, mode="wt")
        f.write(self.format())
        f.close()

    def format(self):
        lines = []
        for row in self.matrix:
            line_items = []
            for n in row:
                line_items.append(str(n))
            line = " ".join(line_items)
            lines.append(line)
        return "\n".join(lines)

    def load(self, filename):
        f = open(filename, mode="rt")
        text = f.readlines()
        for idx, _ in enumerate(text):
            text_array = text[idx].split()
            small_matrix = []
            for idx, _ in enumerate(text_array):
                small_matrix.append(int(text_array[idx]))
            self.matrix.append(small_matrix)
        f.close()

if __name__ == "__main__":
    a = MyMatrix([[1, 2, 3], [4, 5, 6]])
    a.print_matrix()
    a.save("test")
    b = MyMatrix()
    b.load("test")
    b.print_matrix()