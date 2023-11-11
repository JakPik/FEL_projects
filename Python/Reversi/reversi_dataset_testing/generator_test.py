def gen(size):
    for r in range(size):
        for c in range(size):
            yield r, c

def sizes(a):
    a = update(a)
    return a, a + 1

def update(a):
    a += 5
    return a

for r, c in gen(8):
    print(r," and ", c)

number = 0
a = []
b = [1]
if(not a):
    print("zes")
if(not b):
    print("bba")

num_1, num_2 = sizes(number)

print(num_1)
print(num_2)