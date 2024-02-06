import matplotlib.pyplot as plt

x = [1, 1, 5, 5, 1]
y = [1, 5, 5, 1, 1]
plt.figure(figsize=(7, 7))
plt.plot(x, y, marker='o')
plt.title('КВАДРАТ')
plt.savefig('fig_task_1.png')
