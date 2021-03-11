# y = ax+b
# y = B * pow(x, a)
# y = B + pow(e, a*x)
# y = a*pow(2) + b*x + c
# Точность: 0,0001. Значения a, b, c округлить до 0,01.
# Построить график.

import math
import matplotlib.pyplot as plt


def determ2(delta):
    return (delta[0][0] * delta[1][1] - delta[0][1] * delta[1][0])


def determ3(delta):
    a = b = c = ai = bi = ci = 1
    for i in range(0, 3):
        a *= delta[i][i]
        if (i < 2):
            b *= delta[i][i + 1]
        if (i > 0):
            c *= delta[i][i - 1]
        if (i < 2):
            ai *= delta[i][2 - i]
        if (i < 2):
            bi *= delta[i][1 - i]
        if (i > 0):
            ci *= delta[i][3 - i]
    b *= delta[2][0]
    c *= delta[0][2]
    ai *= delta[2][0]
    bi *= delta[2][2]
    ci *= delta[0][0]
    return (a + b + c - ai - bi - ci)


def sum_list(data_list, j=1, log=1):
    if (log == 1):
        sum_l = round(sum([i ** j for i in data_list]), 4)
    else:
        sum_l = round(sum([math.log(i) ** j for i in data_list]), 4)
    return sum_l


def sum_two_list(f_data, s_data, j=1):
    sum_l = round(sum([(i ** j) * s_data[f_data.index(i)] for i in f_data]), 4)
    return sum_l


def line_fun(list_x, list_y, plt, legend):
    sum_x = sum_list(list_x)
    sum_y = sum_list(list_y)
    sum_x_2 = sum_list(list_x, 2)
    sum_x_y = sum_two_list(list_x, list_y)
    line = len(list_x)
    determine = determ2([[sum_x_2, sum_x], [sum_x, line]])
    if determine != 0:
        a = determ2([[sum_x_y, sum_x], [sum_y, line]]) / determine
        b = determ2([[sum_x_2, sum_x_y], [sum_x, sum_y]]) / determine
        y = [(a * i + b) for i in range(1, line + 1)]  # f(x[i])
        s = [(list_y[i] - y[i]) ** 2 for i in range(line)]  # (y[i] - f(x[i])) ** 2
        S = round(sum(s), 3)
        legend.append(f"Линейная функция S = {S}")
        plt.plot(list_x, y, linewidth=2)
        return S
    else:
        return -1


def degree_fun(list_x, list_y, plt, legend):
    sum_x = sum_list(list_x, 1, 'l')
    sum_y = sum_list(list_y, 1, 'l')
    sum_x_2 = sum_list(list_x, 2, 'l')
    sum_x_y = round(sum([math.log(i) * math.log(list_y[list_x.index(i)]) for i in list_x]), 4)
    line = len(list_x)
    determine = determ2([[sum_x_2, sum_x], [sum_x, line]])
    if determine != 0:
        a = determ2([[sum_x_y, sum_x], [sum_y, line]]) / determine
        b = math.exp(round(determ2([[sum_x_2, sum_x_y], [sum_x, sum_y]]) / determine, 4))
        y = [b * pow(a, i) for i in list_x]  # f(x[i])
        s = [(list_y[i] - y[i]) ** 2 for i in range(line)]  # (log(y[i]) - f(x[i])) ** 2
        S = round(sum(s), 3)
        legend.append(f"Степеная функция S = {S}")
        plt.plot(list_x, y, linewidth=2)
        return S
    else:
        return -1


def exp_fun(list_x, list_y, plt, legend):
    sum_x = sum_list(list_x)
    sum_y = sum_list(list_y, 1, 'l')
    sum_x_2 = sum_list(list_x, 2)
    sum_x_y = round(sum([i * math.log(list_y[list_x.index(i)]) for i in list_x]), 4)
    line = len(list_x)
    determine = determ2([[sum_x_2, sum_x], [sum_x, line]])
    if determine != 0:
        a = round(determ2([[sum_x_y, sum_x], [sum_y, line]]) / determine, 4)
        b = math.exp(round(determ2([[sum_x_2, sum_x_y], [sum_x, sum_y]]) / determine, 4))

        y = [b * pow(math.exp(1), a * i) for i in list_x]  # f(x[i])
        s = [(list_y[i] - y[i]) ** 2 for i in range(line)]  # (log(y[i]) - f(x[i])) ** 2
        S = round(sum(s), 3)
        legend.append(f"Показательная функция S = {S}")
        plt.plot(list_x, y, linewidth=2)
        return S
    else:
        return -1


def quad_fun(list_x, list_y, plt, legend):
    sum_x = sum_list(list_x)
    sum_y = sum_list(list_y)
    sum_x_2 = sum_list(list_x, 2)
    sum_x_3 = sum_list(list_x, 3)
    sum_x_4 = sum_list(list_x, 4)
    sum_x_y = sum_two_list(list_x, list_y)
    sum_x_2_y = sum_two_list(list_x, list_y, 2)
    line = len(list_x)
    determine = determ3([[sum_x_4, sum_x_3, sum_x_2], [sum_x_3, sum_x_2, sum_x], [sum_x_2, sum_x, line]])
    if determine != 0:
        a = round(determ3([[sum_x_2_y, sum_x_y, sum_y], [sum_x_3, sum_x_2, sum_x], [sum_x_2, sum_x, line]]) / determine,
                  2)
        b = round(
            determ3([[sum_x_4, sum_x_2_y, sum_x_2], [sum_x_3, sum_x_y, sum_x], [sum_x_2, sum_y, line]]) / determine, 2)
        c = round(
            determ3([[sum_x_4, sum_x_3, sum_x_2_y], [sum_x_3, sum_x_2, sum_x_y], [sum_x_2, sum_x, sum_y]]) / determine,
            2)
        y = [(a * i ** 2 + b * i + c) for i in range(1, line + 1)]  # f(x[i])
        s = [(list_y[i] - y[i]) ** 2 for i in range(line)]  # (y[i] - f(x[i])) ** 2
        S = round(sum(s), 3)
        legend.append(f"Квадратичная функция S = {S}")
        plt.plot(list_x, y, linewidth=2)
        return S
    else:
        return -1


plt.figure(figsize=(12, 8))
plt.title("Least squares method")
plt.xlabel("X")
plt.ylabel("Y")
plt.autoscale(tight=True)
n = int(input("Введите количество точек: "))
legend = []
list_x = [i for i in range(1, n + 1)]
list_y = list(map(float, input("Введите значение вектора y: ").split()))
line_fun(list_x, list_y, plt, legend)
degree_fun(list_x, list_y, plt, legend)
exp_fun(list_x, list_y, plt, legend)
quad_fun(list_x, list_y, plt, legend)
plt.plot(list_x, list_y, 'D')
legend.append("Данные")
plt.legend(legend, loc="upper left")
plt.grid()
plt.savefig('data_1.png', dpi=50)
plt.show()
# n = int(input("Введите количество точек: "))
# list_x = [i for i in range(1, n + 1)]
# list_y = list(map(float, input("Введите значение вектора y: ").split()))
# print(line_fun(list_x, list_y))
# print(degree_fun(list_x, list_y))
# print(exp_fun(list_x, list_y))
# print(quad_fun(list_x, list_y))
