# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import random
import time

f = time.time()
n = 1000
t = {j: (random.uniform(0.0, 36.0), random.uniform(0.0, 36.0)) for j in range(n)}
s = time.time()
print(f"random.uniform(0.0, 36.0): {s - f}")
f = time.time()
x = [i / 1000000.0 for i in range(0, 36000000)]
y = [i / 1000000.0 for i in range(0, 18000000)]
t = {j: (random.choice(x), random.choice(y)) for j in range(n)}
s = time.time()
print(f"random.uniform(0.0, 36.0): {s - f}")