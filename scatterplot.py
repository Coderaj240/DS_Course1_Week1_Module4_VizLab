import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)
retirement_age =5 *np.random.randn(200)+65
life_expectancy=np.random.randint(74,101,size=200)

plt.scatter(retirement_age,life_expectancy,c='blue',alpha=0.7)
plt.xlabel('Retirement Age')
plt.ylabel('Life Expectancy')
plt.title('age & life life_expectancy relation')
plt.show()