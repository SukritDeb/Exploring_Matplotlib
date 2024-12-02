from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()

values = [12, 55, 4, 22, 104]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0]
labels = ['India', 'United States', 'Russia', 'China', 'UK']
plt.pie(values, colors= colors, labels=labels, explode = explode)
plt.title('Student Locations')
plt.show()