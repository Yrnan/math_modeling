import numpy as np
g = 9.8

def maxenergy(m, h, v0):
    E_k = (m * v0 ** 2)/2
    E_p = m * g * h
    E = E_k + E_p
    print(E)
    
m = 20
h = 15
v0 = 60

maxenergy(m, h, v0)