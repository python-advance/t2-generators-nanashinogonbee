def list_comprehension_fibonacci(num):
    order = int(''.join(i for i in order if i.isdigit()))
    fib = [0, 1]
    fib += [fib.append(fib[_-2] + fib[_-1]) for _ in range(2, order)]
    fib = [item for item in fib if isinstance(item, int)]


def generator_fibonacci(num):
    fib1, fib2 = 0, 1
    for i in range(num):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1
