import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
x=5*np.random.randn(200)+65
plt.hist(x,bins=5,edgecolor='pink')

plt.xlabel('Retirement Age')
plt.ylabel('Frequency of values')
plt.title('histogram in Matplotlib of 200 people')
plt.show()
