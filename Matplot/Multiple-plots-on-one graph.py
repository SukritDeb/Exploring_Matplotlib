from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

plt.plot(x, norm.pdf(x)) #first line plotting
plt.plot(x, norm.pdf(x, 1.0, 0.5)) #second line plotting
plt.show()
