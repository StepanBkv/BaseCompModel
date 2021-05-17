import random
import matplotlib.pyplot as plt
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
    plt.hist(y_list)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def random_def_2(n=100):
    y = [((2 ** 30) * x / (n * 10)) % 1 for x in range(1, n)]
    plt.hist(y)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def rand_num_Neiman(n=5):
    y = 7153
    y_list = [y / (10 ** 4)]
    for i in range(n):
        y = ((y ** 2) // 10 ** 2) % 10 ** 4
        y_list.append(y / (10 ** 4))
    plt.hist(y_list)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def multi_kong_met(n=100):
    m_1 = 1357
    m_l = [m_1 / 10000]
    for i in range(n):
        m_1 = ((1357 * m_1) % 9999)
        m_l.append(m_1 / 10000)
    plt.hist(m_l)
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


n = input("Введите кол-во случайных чисел для 1 метода: ")
random_def_1(int(n))
n = input("Введите кол-во случайных чисел для 2 метода: ")
random_def_2(int(n))
n = input("Введите кол-во случайных чисел для метода Неймана: ")
rand_num_Neiman(int(n))
n = input("Введите кол-во случайных чисел для мультипликативного конгруэнтного метода: ")
multi_kong_met(int(n))
# реализация первых 4 методов практики.