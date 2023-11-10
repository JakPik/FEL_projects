def gen(size):
    for r in range(size):
        for c in range(size):
            yield r, c

for r, c in gen(8):
    print(r," and ", c)