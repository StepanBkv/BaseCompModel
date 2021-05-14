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
    y_list = [y]
    for i in range(n):
        y_1 = formula(y) % 1
        y = y_1
        y_list.append(y)
    plt.plot([x for x in range(n+1)], y_list)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def random_def_2(n=100):
    y = [((2 ** 30) * x / (n * 10)) % 1 for x in range(1, n)]
    plt.plot([x for x in range(1, n)], y)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def rand_num_Neiman(n=5):
    y = 7153
    y_list = [y / (10 ** 4)]
    for i in range(n):
        y = ((y ** 2) // 10 ** 2) % 10 ** 4
        y_list.append(y / (10 ** 4))
    plt.plot([x for x in range(n+1)], y_list)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()

def random_def_4(n=100):
    m_1 = 1357
    m_l = [m_1/1000]
    for i in range(n):
        m_1 = ((1357 * m_1) / 5689)
        m_l.append(m_1 / 1000)
    plt.plot([x for x in range(n + 1)], m_l)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()

random_def_4(10)
