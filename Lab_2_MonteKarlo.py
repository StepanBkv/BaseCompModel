import random
# from src.basicGraphs import loadPrices
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


def equality(first, second):
    return first == second


def is_sublist(first, second):
    for i in range(len(first)):
        if first[i] == second[0]:
            if all([first[i + j] == second[j] for j in range(1, len(second))]):
                return True
    return False


print(is_sublist([1, 2, 3, 1, 2, 3, 4, 5], [1, 2, 3, 4]))
