import numpy as np

L = [8, 1, 6, 9, 0, 3]
list = np.array(L)

def avg(n):
    m = np.average(n)
    print(m)

avg(list)