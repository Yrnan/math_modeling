import matplotlib.pyplot as plt 
import numpy as np 


R = 1

t = np.arange(0, 10, 0.01)

x = R*t - R*np.sin(t)
y = R - R*np.cos(t)


plt.figure(figsize=(7, 7))
plt.axis('equal')
plt.plot(x, y)
plt.title('ЦИКЛОИДА')
plt.savefig('task_1-1.png')
    


























