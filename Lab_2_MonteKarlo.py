import random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy
import math


def formula(x):
    return math.sqrt(29 - math.cos(x) ** 2)


def opredel_integral(a, b, n):
    plt.figure(figsize=(12, 8))
    plt.title("Monte - Karlo")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.autoscale(tight=True)
    legend = []
    plt.plot([formula(i) for i in range(b)], [i for i in range(b)])
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()
    return ((b - a) / n) * sum([formula(random.uniform(float(a), float(b))) for i in range(n)])


def monte_karlo_1():
    n = 100000
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


def monte_karlo_2():
    a = 36
    b = 18
    n = 10000000
    random_list = [i / 10000.0 for i in range(1000000)]
    # x = [i / 1000000.0 for i in range(0, 36000000)]
    # y = [i / 1000000.0 for i in range(0, 18000000)]
    # t = {j: (random.choice(x), random.choice(y)) for j in range(n)}
    # method = "random.choise"
    t = {j: (random.uniform(0.0, 36.0), random.uniform(0.0, 18.0)) for j in range(n)}
    method = "random.uniform"
    got = [[t[key][0], t[key][1]] for key in t if (10 * ((t[key][0] - 20) / -8) + 20 > t[key][1] < 10 * t[key][0] / 12)]
    dot_got = [[t[key][0], t[key][1]] for key in t if
               (10 * ((t[key][0] - 20) / -8) + 20 <= t[key][1] or t[key][1] >= 10 * t[key][0] / 12)]
    def_1 = [10 * random_list[i] / 12 for i in range(1000000)]
    def_2 = [10 * ((random_list[i] - 20) / -8) + 20 for i in range(1000000)]

    plt.figure(figsize=(12, 8))
    plt.title("Monte - Karlo")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.autoscale(tight=True)
    legend = []

    legend.append("Случайные точки")
    f = (len(got) / (len(got) + len(dot_got))) * a * b
    print(len(got) / len(got) + len(dot_got))
    s = (18 * 36) / 2

    legend.append(f"Площадь треугольника {method} S = {f}, {s}, Погрешность:{abs(s - f) / f}")
    plt.scatter([key[0] for key in got], [key[1] for key in got], s=5, c="blue")
    plt.scatter([key[0] for key in dot_got], [key[1] for key in dot_got], s=5, c="green")
    plt.plot(random_list, def_1)
    plt.plot(random_list, def_2)
    print(f"Дисперсия X: {numpy.nanmean([t[key][0] for key in t])}",
          f"Мат.ожидание X: {numpy.nanvar([t[key][0] for key in t])}")
    print(f"Дисперсия Y: {numpy.nanmean([t[key][1] for key in t])}",
          f"Мат.ожидание Y: {numpy.nanvar([t[key][1] for key in t])}")
    print(f"Вычисление дисперсии по формулам X: {18}",
          f"Вычисление мат.ожидания X: {36 ** 2 / 12}")
    print(f"Вычисление дисперсии по формулам Y: {9}",
          f"Вычисление мат.ожидания Y: {18 ** 2 / 12}")
    plt.plot([0, 36], [0, 0])
    plt.plot([0, 36], [18, 18])
    plt.plot([36, 36], [0, 18])
    plt.plot([0, 0], [0, 18])
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def circle(r, n):
    plt.figure(figsize=(12, 8))
    plt.title("Monte - Karlo")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.autoscale(tight=False)
    legend = []
    circle_list = [x / 10.0 for x in range(r * 100)]
    plt.plot([r * math.cos(x) for x in circle_list], [r * math.sin(x) for x in circle_list])
    legend.append("Круг")
    plt.legend(legend, loc="upper left")
    plt.plot([-r, -r], [-r, r])
    plt.plot([-r, r], [-r, -r])
    plt.plot([r, -r], [r, r])
    plt.plot([r, r], [-r, r])
    t = {j: (random.uniform(-2.0, 2.0), random.uniform(-2.0, 2.0)) for j in range(n)}
    got = [[t[key][0], t[key][1]] for key in t if ((t[key][0])) ** 2 + (t[key][1]) ** 2 <= r ** 2]
    dot_got = [[t[key][0], t[key][1]] for key in t if (abs(t[key][0])) ** 2 + (abs(t[key][1])) ** 2 > r ** 2]

    plt.scatter([key[0] for key in got], [key[1] for key in got], s=5, c="blue")
    plt.scatter([key[0] for key in dot_got], [key[1] for key in dot_got], s=5, c="brown")
    print(f" PI : {(len(got) / (len(dot_got) + len(got))) * 4}")
    plt.grid()
    # plt.show()


def formul_p(x, a=23, b=19):
    return math.sqrt(abs(a * math.cos(x) + b * math.sin(x)))


def formula_p_sin(x, a, b):
    return formul_p(x, a, b) * math.sin(x)


def formula_p_cos(x, a, b):
    return formul_p(x, a, b) * math.cos(x)


def figur(n, a, b):
    plt.figure(figsize=(12, 8))
    plt.title("Monte - Karlo")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.autoscale(tight=False)
    legend = []
    pi_list = [i / 100.0 for i in range(int(2 * math.pi * 100))]
    x = [formul_p(i, a, b) * math.cos(i) for i in pi_list]
    y = [formul_p(i, a, b) * math.sin(i) for i in pi_list]
    plt.plot(x, y)
    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)
    plt.plot([min_x, max_x, max_x, min_x, min_x], [min_y, min_y, max_y, max_y, min_y])
    t = {j: (formula_p_cos(random.uniform(0, 2 * math.pi), a, b), formula_p_sin(random.uniform(0, 2 * math.pi), a, b))
         for j in range(n)}
    got = [[t[key][0], t[key][1]] for key in t if
           (math.sqrt(t[key][0] ** 2 + t[key][1] ** 2)) < formul_p(numpy.arctan(t[key][1] / t[key][0]), a, b)]
    dot_got = [[t[key][0], t[key][1]] for key in t if
               (math.sqrt(t[key][0] ** 2 + t[key][1] ** 2)) >= formul_p(numpy.arctan(t[key][1] / t[key][0]), a, b)]
    plt.scatter([key[0] for key in got], [key[1] for key in got], s=5, c="blue")
    plt.scatter([key[0] for key in dot_got], [key[1] for key in dot_got], s=5, c="brown")
    legend.append("Фигура")
    legend.append(
        f"Площадь S: {round(len(got) / ((len(got)) + len(dot_got)) * (abs(max_x - min_x)) * abs(max_y - min_y), 3)}")
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


figur(1000000, 13, 9)
