import matplotlib.pyplot as plt 
import numpy as np


R = 1

t = np.arange(0, 10, 0.01)

x = R * np.cos(t)**3
y = R * np.sin(t)**3


plt.figure(figsize=(7, 7))
plt.axis('equal')
plt.plot(x, y)
plt.title('АСТРОИДА')
plt.savefig('task_1-2.png')