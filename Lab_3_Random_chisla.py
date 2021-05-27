import random
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.title("Monte - Karlo")
plt.xlabel("X")
plt.ylabel("Y")
plt.autoscale(tight=False)
legend = []


def rand_num_Neiman(n=20):
    y = 7153
    y_list = [y / (10 ** 4)]
    for i in range(n):
        y = ((y ** 2) // 10 ** 2) % 10 ** 4
        y_list.append(y / (10 ** 4))
    plt.hist(y_list)
    plt.title("Метод Неймана")
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def multi_kong_met(n=1000):
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
    plt.hist(data)
    plt.title("Конгуэтный Мультипликативный Метод")
    plt.legend(legend, loc="upper left")
    plt.grid()
    plt.show()


def method_proizveden(n=10000):
    core = 5167
    multi_plex = 3729
    data = []
    for i in range(n):
        a = (multi_plex * core) % 10 ** 6
        multi_plex = a % 10 ** 4
        data += [(a // 10 ** 2) / 10 ** 4]
    plt.hist(data, color='blue', edgecolor='black', bins=40)
    plt.title("Метод Произведений")
    plt.legend(legend, loc="upper left")
    plt.tight_layout()
    plt.grid()
    plt.show()


def kong_met(n=999):
    x = 1
    data = []
    for i in range(1, n):
        x = ((2 ** 30) * x / (n * 10)) % 1
        data += [x]
    plt.hist(data, color='blue', edgecolor='black', bins=4)
    plt.legend(legend, loc="upper left")
    plt.title("Конгруэнтный Метод")
    plt.tight_layout()
    plt.grid()
    plt.show()


def len_kong_met(n=1999):
    x = 1221
    a = 2 ** 30
    c = 4354
    m = 10000000
    data = []
    for i in range(1, n):
        x = ((a * x + c) / m) % 1
        data += [x]
    print(data)
    plt.hist(data, color='blue', edgecolor='black', bins=4)
    plt.legend(legend, loc="upper left")
    plt.title("Линейный Конгруэнтный Метод")
    plt.tight_layout()
    plt.grid()
    plt.show()


def random_def_2(n=100):
    y = [((2 ** 30) * x / (n * 10)) % 1 for x in range(1, n)]
    plt.hist(y)
def rand(n):
    data = [random.random() for i in range(n)]
    print(data)
    plt.hist(data, color='blue', edgecolor='black', bins=4)
    plt.legend(legend, loc="upper left")
    plt.title("Встроенный Метод")
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

n = input("Введите кол-во случайных чисел для Метода Неймана: ")
rand_num_Neiman(int(n))
n = input("Введите кол-во случайных чисел для Метода Произведений: ")
method_proizveden(int(n))
n = input("Введите кол-во случайных чисел для Мультипликативного конгруэнтного метода: ")
multi_kong_met(int(n))
n = input("Введите кол-во случайных чисел для Конгруэтного метода: ")
kong_met(int(n))
n = input("Введите кол-во случайных чисел для Линейного Конгруэтного Метода: ")
len_kong_met(int(n))
n = input("Введите кол-во случайных чисел для встроенного метода: ")
rand(int(n))
