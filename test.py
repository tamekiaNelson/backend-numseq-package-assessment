#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Numseq assignment"""

__author__ = "tamekiaNelson"


from numseq.fib import fib
from numseq.geo import *
from numseq.prime import *
import time


def timeit(f):
    def timer(*args, **kw):
        ts = time.time()
        results = f(*args, **kw)
        te = time.time()
        print 'func:%r args:[%r, %r] took: %2.4f sec' % \
            (f.__name__, args, kw, te-ts)
        return results
    return timer
#borrowed timer func from online to make sure program was running below 1 sec


@timeit
def main():
    print("Fibonacci")
    for i in range(10):
        print("{}: {}".format(i, fib(i)))
    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))
    print("Primes")
    prime_list = prime(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    main()
