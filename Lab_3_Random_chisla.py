import random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy
import math


def formula(x):
    return math.exp(x ** 2 + x + 5)


plt.figure(figsize=(12, 8))
plt.title("Monte - Karlo")
plt.xlabel("X")
plt.ylabel("Y")
plt.autoscale(tight=False)
legend = []


def random_def_1(n=10000):
    y = 0
    for i in range(n):
        y_1 = formula(y) % 1
        y = y_1
        print(y)


def random_def_2(n=10000):
    y = [((2 ** 30) * x / (n * 10)) % 1 for x in range(1, n)]
    print(y)


def rand_num_Neiman(n=5):
    y = 7153
    for i in range(n):
        y = ((y ** 2) // 10 ** 2) % 10 ** 4
        print(y / (10 ** 4))


def random_def_4(n=100):
    m_1 = 1357
    m_l = []
    for i in range(n):
        m_1 = ((1357 * m_1) % 5689)
        m_l.append(m_1 / 10000)
        print(m_l)


rand_num_Neiman(1)
