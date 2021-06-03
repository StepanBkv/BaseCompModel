import matplotlib.pyplot as plt
import numpy as np
import math

# Входные данные

def f(x, y, z):
    return -2*y + 4*z

def g(x, y, z):
    return -y + 3*z

y_0 = 3.0
z_0 = 0.0

end_int = input("Введите последнее значение для построения графиков: ") # Последнее значение для построения графиков
step = input("Введите кол-во шагов (разбиений): ") # Количество шагов

def realY(t):
    return 4 * math.exp(-t) - math.exp(2*t)

def realZ(t):
    return math.exp(-t) - math.exp(2*t)

# Вычисление точек

x, h = np.linspace(0, end_int, step, retstep=True)
y = [y_0]
z = [z_0]

for i in range(len(x) - 1):

    i1 = h * f(x[i], y[i], z[i])
    l1 = h * g(x[i], y[i], z[i])

    i2 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * i1, z[i] + 0.5 * l1)
    l2 = h * g(x[i] + 0.5 * h, y[i] + 0.5 * i1, z[i] + 0.5 * l1)

    i3 = h * f(x[i] + 0.5 * h, y[i] + 0.5 * i2, z[i] + 0.5 * l2)
    l3 = h * g(x[i] + 0.5 * h, y[i] + 0.5 * i2, z[i] + 0.5 * l2)

    i4 = h * f(x[i] + h, y[i] + i3, z[i] + l3)
    l4 = h * f(x[i] + h, y[i] + i3, z[i] + l3)

    dy = (1.0 / 6.0) * (i1 + 2*i2 + 2*i3 + i4)
    dz = (1.0 / 6.0) * (l1 + 2*l2 + 2*l3 + l4)

    y.append(y[i] + dy)
    z.append(z[i] + dz)


# График уравнения
plt.plot(x, [realY(i) for i in x], c="blue")
plt.plot(x, y, c="blue", ls="--")
plt.plot(x, [realZ(i) for i in x], c="red")
plt.plot(x, z, c="red", ls="--")

plt.grid(True)
plt.show()