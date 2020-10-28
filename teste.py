import time


def fatrecur(n):
    if n == 0:
        return 1
    else:
        res = n * fatrecur(n - 1)
        return res


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input('digite um numero'))
start = time.time()
# print(start, ' - start')
print(fib(n))
elapsed = time.time() - start
print(elapsed, ' - elapsed')
# 0-1-1-2-3-5-8-13-21-34-55-89-144
