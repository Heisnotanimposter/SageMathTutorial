import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return np.sin(x) / x

x = np.linspace(-10, 10, 100)
y = h(x)

plt.plot(x, y)
plt.ylim(-1.2, 1.2)
plt.xlabel('x')
plt.ylabel('h(x)')
plt.show()
