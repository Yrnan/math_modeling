import numpy as np
from Lab_3_task_1 import g

h = 100
a = np.pi/3
b = 30

chisl = g * h * np.tan(b)**2
znam = 2 * np.cos(a)**2 * ( 1 - np.tan(b) * np.tan(a) )
v = chisl/znam
otv = v**0.5

print(otv)