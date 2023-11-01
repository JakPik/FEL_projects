def generate_fib(n):
    a, b = (0, 1)
    for i in range(n):
        yield a
        a, b = (b, a + b)

##Test of git

if __name__ == '__main__':
    for num in generate_fib(10):
        print(num)