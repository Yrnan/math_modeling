from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


xdata, ydata = [], []

def animate(t):
    xdata.append(np.sin(t)*((np.e**np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    ydata.append(np.cos(t)*((np.e**np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    fly.set_data(xdata, ydata)
    return fly


if __name__ == '__main__':
    fig, ax = plt.subplots(figsize = (7, 7))
    fly, = plt.plot([], [], '-', color='b', label='Ball')
    edge = 5
    plt.figure(figsize=(7, 7))
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 12*np.pi, 0.1),
                        interval=30
                        )
    ani.save('task_3-1.gif') 