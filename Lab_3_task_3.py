import numpy as np 
from Lab_3_task_1 import g

x_0 = 0
y_0 = 0
v_0x = 0
t = np.arange(0.5, 0.1)

x = x_0 + v_0x*t 
y = y_0 + v_0x*t - ((g * t ** 2) / 2)

a = [t, x, y]
b = np.array(a)

print(type(a))
print(type(b))