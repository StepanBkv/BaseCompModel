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
    random_list = [i / 10000000.0 for i in range(0, 50000000)]
    return ((b - a) / n) * sum([formula(random.choice(random_list)) for i in range(n)])


def monte_karlo():
    # b = 5
    # a = 0
    # x = random.randint(0, 5)
    # y = random.randint(0, 5)
    # k = x + (y - x) * n
    # t = {j: [random.randint(x, y): random.randint(x, y)] for j in range(n)}
    # print(t)
    n = 10000000
    x = [i / 1000000.0 for i in range(0, 20000000)]
    # список с значениями float из которого будут выбираться случайный значения x
    y = [10 * x[i] / 2 if 0 <= x[i] < 2 else 10 * ((x[i] - 20) / -18) if 2 <= x[i] < 20 else 0 for i in
         range(0, 2000000)]
    # список с значениями float из которго будут выбираться случайные значения y
    # print({x[i]: y[i] for i in range(2000000)})
    random_list_y = [i / 1000000.0 for i in range(0, 10000000)]
    t = {j: (random.choice(x), random.choice(random_list_y)) for j in range(n)}
    N = [
        True if (0 <= t[key][0] < 2 and t[key][1] < (10 * t[key][0]) / 2) or (2 <= t[key][0] < 20 and t[key][1] < 10 * (
                t[key][0] - 20) / -18) else False for key in t]
    plt.figure(figsize=(12, 8))
    plt.title("Monte - Karlo")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.autoscale(tight=True)
    legend = []
    plt.plot([t[key][0] for key in t], [t[key][1] for key in t], 'D')  # постановка случайных точкек на плоскость
    plt.plot(x, y, 'D')  # график пересекающихся функций
    legend.append("Случайные точки")
    # вывод площади треугольника с помощью двух методов Монте - Карло
    legend.append(
        f"Площадь треугольника S = {(len([i for i in N if i]) / len(N)) * 20 * 10} |"
        f" {(20 / n) * sum([random.choice(y) for i in range(n)])}")
    # вывод...
    # ограничивающие линии
    plt.plot([0, 20], [10, 10])
    plt.plot([20, 20], [0, 10])
    plt.plot([0, 0], [0, 10])
    plt.plot([0, 20], [0, 0])
    # показывающие где мы считаем график функции
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


a = 36
b = 18
n = 1000
random_list = [i / 10000.0 for i in range(1000000)]
# x = [i / 1000000.0 for i in range(0, 36000000)]
# y = [i / 1000000.0 for i in range(0, 18000000)]
# t = {j: (random.choice(x), random.choice(y)) for j in range(n)}
t = {j: (random.uniform(0.0, 36.0), random.uniform(0.0, 18.0)) for j in range(n)}
N = [True if 10 * ((t[key][0] - 20) / -8) + 20 > t[key][1] < 10 * t[key][0] / 12 else False for key in t]
def_1 = [10 * random_list[i] / 12 for i in range(1000000)]
def_2 = [10 * ((random_list[i] - 20) / -8) + 20 for i in range(1000000)]
plt.figure(figsize=(12, 8))
plt.title("Monte - Karlo")
plt.xlabel("X")
plt.ylabel("Y")
plt.autoscale(tight=True)
legend = []
legend.append("Случайные точки")
f = (len([i for i in N if i]) / len(N)) * a * b
s = (18*36)/2
legend.append(f"Площадь треугольника S = {f}, {s}, Погрешность:{(s - f) ** 2}")
plt.plot([t[key][0] for key in t], [t[key][1] for key in t], 'D')
plt.plot(random_list, def_1)
plt.plot(random_list, def_2)
print(f"Дисперсия X: {numpy.nanmean([t[key][0] for key in t])}",
      f"Мат.ожидание X: {numpy.nanvar([t[key][0] for key in t])}")
print(f"Дисперсия Y: {numpy.nanmean([t[key][1] for key in t])}",
      f"Мат.ожидание Y: {numpy.nanvar([t[key][1] for key in t])}")
print(f"Вычисление дисперсии по формулам: {18}", f"Вычисление мат.ожидания: {36 ** 2 / 12}")
plt.plot([0, 36], [0, 0])
plt.plot([0, 36], [18, 18])
plt.plot([36, 36], [0, 18])
plt.plot([0, 0], [0, 18])
plt.legend(legend, loc="upper left")
plt.grid()
plt.show()
