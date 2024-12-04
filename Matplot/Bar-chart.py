from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

values = [120, 55, 4, 32, 140]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0,5), values, color= colors) #plots bar chart
plt.show()
