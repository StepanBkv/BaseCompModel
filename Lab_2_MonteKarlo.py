import random
# from src.basicGraphs import loadPrices
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import numpy
import math


def formula(x):
    return math.cos(x) + x ** 2


def opredel_integral(a, b, n):
    random_list = [i / 10000000.0 for i in range(0, 50000000, 1)]
    return ((b - a) / n) * sum([formula(random.choice(random_list)) for i in range(n)])


# b = 5
# a = 0
# x = random.randint(0, 5)
# y = random.randint(0, 5)
# k = x + (y - x) * n
# t = {j: [random.randint(x, y): random.randint(x, y)] for j in range(n)}
# print(t)
n = 100000
x = [i / 100000.0 for i in range(0, 2000000)]
y = [10 * x[i] / 2 if 0 <= x[i] < 2 else 10 * ((x[i] - 20) / -18) if 2 <= x[i] < 20 else 0 for i in range(0, 2000000)]
# print({x[i]: y[i] for i in range(2000000)})
random_list_x = [i / 1000000.0 for i in range(0, 20000000)]
random_list_y = [i / 1000000.0 for i in range(0, 10000000)]
t = {j: (random.choice(random_list_x), random.choice(random_list_y)) for j in range(n)}
N = [True if (0 <= t[key][0] < 2 and t[key][1] <= (10 * t[key][0]) / 2) or ( 2 <= t[key][0] < 20 and t[key][1] <= 10 * (
            t[key][0] - 20) / -18) else False for key in t]
plt.figure(figsize=(12, 8))
plt.title("Monte - Karlo")
plt.xlabel("X")
plt.ylabel("Y")
plt.autoscale(tight=True)
legend = []
plt.plot([t[key][0] for key in t], [t[key][1] for key in t], 'D')
plt.plot(x, y, 'D')
legend.append("Случайные точки")
legend.append(f"Площадь треугольника S = {(len([i for i in N if i])/len(N)) * 20 * 10}")
plt.plot([0, 20], [10, 10])
plt.plot([20, 20], [0, 10])
plt.plot([0, 0], [0, 10])
plt.plot([0, 20], [0, 0])
plt.legend(legend, loc="upper left")
plt.grid()
plt.show()
