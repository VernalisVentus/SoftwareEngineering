def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 200
fib_gen = fib(n)
fib_list = list(fib_gen)
print(f"200-е число Фибоначчи: {fib_list[-1]}")
