# Wojciech Szlosek

import math
import matplotlib.pyplot as plt
import numpy
import statistics
import numpy as np
import scipy.stats as st
from statsmodels.sandbox.stats.runs import runstest_1samp

class RandomNumberGenerator:

    def __init__(self, a=16807, n=2147483647, seed=555):
        self.out = seed
        self.a = a
        self.n = n

    def __next__(self):
        self.out = self.a * self.out % self.n
        return self.out


class UniformNumberGenerator(RandomNumberGenerator):

    def __next__(self, a=0, b=1):

        if a == 0 and b == 1:
            return super(UniformNumberGenerator, self).__next__()/self.n

        lxy = b-a+1

        return ((super(UniformNumberGenerator, self).__next__()/self.n)*lxy + a)


class Bernoulli:

    def __init__(self):
        self.u = UniformNumberGenerator()

    def __next__(self, p):
        if self.u.__next__() <= p:
            return 1
        else:
            return 0

class Binomial:

    def __init__(self):
        self.u = UniformNumberGenerator()

    def run(self, p, N):
        x = 0
        for i in range(N):
            if self.u.__next__() <= p:
                x += 1

        return x


class Poisson:

    def __init__(self):
        self.u = UniformNumberGenerator()

    def run(self, lamb):
        x = 0
        w = self.u.__next__()

        while w >= math.exp(-lamb):
            w *= self.u.__next__()
            x += 1

        return x-1


class Exponential:

    def __init__(self):
        self.u = UniformNumberGenerator()


    def run(self):

        u1 = self.u.__next__()
        return -math.log(u1, math.e)


class Normal:
    def __init__(self):
        self.u = UniformNumberGenerator()
        self.v = UniformNumberGenerator()
        self.w = UniformNumberGenerator()

    def run(self):

        w1 = self.u.__next__()
        p1 = 16/((2*math.pi*math.e)**0.5)
        p2 = 0.1108179673
        p4 = 0.0026997960
        p3 = 1-p1-p2-p4
        c1 = 17.4973119
        c2 = 4.73570326
        c3 = 2.15787544
        c4 = 2.36785163
        M = 0.357070192

        if 0 <= w1 and w1 <= p1:
            return (2*w1)/p1 - 1 + self.v.__next__() + self.w.__next__()

        if p1 < w1 and w1 <= (p1+p2):
            return 1.5*((w1-p1)/p2 -1 + self.v.__next__())

        if (1-p4) < w1 and w1 <= 1:
            while True:
                s1 = self.v.__next__()
                s2 = self.w.__next__()
                x = 4.5-math.log(s2,math.e)
                if(x*s1*s1 > 4.5):
                    break

            return (2*x)**(0.5) * numpy.sign(w1-(1-p4/2))

        if p1+p2 < w1 and w1 <= (1-p4):
            while True:
                w1 = self.u.__next__(-3, 3)
                w2 = self.v.__next__()
                v = abs(w1)

                W = (c4/M)*(3-v)*(3-v)
                S = 0

                if v < 1.5:
                    S = (c3/M) * (1.5 - v)
                if v < 1:
                    S = S + (c2/M)*(3-v*v)-W

                if w2 > (c1/M) * math.exp(-v*v)/2 - S - W:
                    break

            return w1

        return 0

    def r2(self):  # rozklad normalny N(0, 1)
        while True:
            w1 = self.u.__next__()
            w2 = self.v.__next__(-((2/math.e)**(0.5)),(2/math.e)**(0.5))
            t = w2/w1

            if w1*w1 > math.exp(-t*t/2):
                break
        return t



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


g = RandomNumberGenerator()
u = UniformNumberGenerator()
b1 = Bernoulli()
b2 = Binomial()
p = Poisson()
ex = Exponential()
nor = Normal()
a = []
b = []
c = []
d = []
e = []
f = []
n = []

for i in range(1000):
    a.append(g.__next__())
    e.append(ex.run())
    n.append(nor.r2())


print(c)
print(a)
print(b)
print(d)
print(e)
print(f)
print(n)

plt.figure(figsize=(10,10))
plt.hist(n, range=[1, 2])
plt.show()