# Wojciech Szlosek

import math
import matplotlib.pyplot as plt
import numpy
import statistics
import numpy as np
import scipy.stats as st
from statsmodels.sandbox.stats.runs import runstest_1samp


def LCG_g(a=7, m=11, x0=1) -> list:
    x = x0
    random_numbers = []

    while True:
        x = (a * x) % m
        random_numbers.append(x)

        if x == x0:
            break


    iterator = iter(random_numbers)

    return iterator


def uniform_generator_j(a=7, m=11, x0=1, i=1000) -> list:
    x = x0
    random_numbers = []

    while i > 0:
        x = (a * x) % m
        random_numbers.append(x/m)

        if x == x0:
            break

        i -= 1

    iterator = iter(random_numbers)

    return iterator


def Bernoulli_b(p, V):
    U = next(V)
    if U < p:
        return 1

    return 0


def binomial_d(N, p):
    x = 0
    U = uniform_generator_j()

    for i in range(N):
        w = next(U)
        if w <= p:
            x += 1

    return x


def Poisson_p(lamb, U1):
    # a First Course in Probability, page 449

    x = 0
    U = next(U1)

    while U >= math.exp(-lamb):
        U *= next(U1)
        x += 1

    return x-1


def exponential_w(t1, t2):  # wykładniczy
    flag = True

    while flag:
        flag = False
        U = v1(0, 1, t1)
        V = v1(0, 2 / math.e, t2)
        x = V/U

        if x <= 2 - 2*U:
            flag = True
        elif x <= 2/U - 2:
            if x <= -2 * math.log(U, math.e):
                flag = True

    return x


def v1(a1, b1, xr1) -> list:  # generator o rozkladzie jednostajnym od a1 do b1
    lxy = b1-a1+1
    xr = next(xr1)
    wxy = (xr*lxy)+a1

    return wxy

def normal_n():
    global x
    flag = True
    U = uniform_generator_j()

    while flag:
        flag = False
        gU = next(U)
        V = v1(-((2/math.e) ** 0.5), ((2 / math.e) ** 0.5))
        x = V/gU

        if x**2 <= 2*(3-gU*(4+gU)):
            flag = True
        elif x**2 <= 2/gU - 2*gU:
            if x**2 <= -4 * math.log(gU, math.e):
                flag = True

    return x


# https://www.codespeedy.com/runs-test-of-randomness-in-python-programming/
def runs_test(l, l_median): # testy serii
    runs, n1, n2 = 0, 0, 0

    for i in range(len(l)):

        # no. of runs
        if (l[i] >= l_median and l[i - 1] < l_median) or (l[i] < l_median and l[i - 1] >= l_median):
            runs += 1

        if (l[i]) >= l_median:
            n1 += 1

        else:
            n2 += 1

    runs_exp = ((2 * n1 * n2) / (n1 + n2)) + 1
    stan_dev = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) /
                         (((n1 + n2) ** 2) * (n1 + n2 - 1)))

    z = (runs - runs_exp) / stan_dev

    return z


xv0 = uniform_generator_j(16807, 2147483647, 133)
V = v1(0, 50, xv0)

print(V)

l = []
xv1 = uniform_generator_j(16807, 2147483647, 133)
for i in range(100):
    t = v1(0, 100, xv1)
    l.append(t)

print(l)
print(f'Z = {abs(runs_test(l, np.median(l)))}') # >= 0.5 czyli ok
