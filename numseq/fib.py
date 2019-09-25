def fib(f):
    if f > 1:
        return fib(f-1) + fib(f-2)
    return f
