import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy.stats import skewnorm

speed = skewnorm.rvs(4, size=50)
size = skewnorm.rvs(4, size=50)

ax = sns.kdeplot(speed, size, cmap="Reds", shade=False, bw=0.15, cbar=True)
ax.set(xlabel='speed', ylabel='size')
plt.show()