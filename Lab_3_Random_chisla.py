import random
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.title("Monte - Karlo")
plt.xlabel("X")
plt.ylabel("Y")
plt.autoscale(tight=False)
legend = []


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
    data = []
    for i in range(n):
        m_1 = ((1357 * m_1) % 5689)
        data.append(m_1 / 10000)
        print(data)
    # plt.hist(data)
    # plt.legend(legend, loc="upper left")
    # plt.grid()
    # plt.show()


def method_proizveden(n=10000):
    core = 5167
    multi_plex = 3729
    data = []
    for i in range(n):
        a = (multi_plex * core) % 10 ** 6
        multi_plex = a % 10 ** 4
        data += [(a // 10 ** 2) / 10 ** 4]
    plt.hist(data, color='blue', edgecolor='black', bins=40)
    plt.legend(legend, loc="upper left")
    plt.tight_layout()
    plt.grid()
    plt.show()


def random_def_2(n=100):
    y = [((2 ** 30) * x / (n * 10)) % 1 for x in range(1, n)]
    plt.hist(y)
    plt.legend(legend, loc="upper left")
    plt.tight_layout()
    plt.grid()
    plt.show()


# n = input("Введите кол-во случайных чисел для 1 метода: ")
# random_def_1(int(n))
# n = input("Введите кол-во случайных чисел для 2 метода: ")
# random_def_2(int(n))
# n = input("Введите кол-во случайных чисел для метода Неймана: ")
# rand_num_Neiman(int(n))
# n = input("Введите кол-во случайных чисел для мультипликативного конгруэнтного метода: ")
# multi_kong_met(int(n))
# реализация первых 4 методов практики.
multi_kong_met(100)
