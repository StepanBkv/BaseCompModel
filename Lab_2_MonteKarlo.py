import random
# from src.basicGraphs import loadPrices
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import numpy
import math


def formula(x):
    return x ** 2 + 2 * x + 3


n = 5000000
b = 5
a = 0
# x = random.randint(0, 5)
# y = random.randint(0, 5)
# k = x + (y - x) * n
# t = {j: {random.randint(x, y): random.randint(x, y)} for j in range(n)}
# print(t)
random_list = [i / 10000000.0 for i in range(0, 50000000, 1)]
square = ((b - a) / n) * sum([formula(random.choice(random_list)) for i in range(n)])
print(square)
