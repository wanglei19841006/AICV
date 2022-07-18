import seaborn as sns
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.DataFrame(np.random.random((10, 6)), 
	                columns=["Iron Man", 
	                         "Captain America", 
	                         "Black Widow",
	                         "Thor",
	                         "Hulk",
	                         "Hawkeye"])
print(data)

heatmap_plot = sns.heatmap(data, center=0, cmap='gist_ncar')

plt.show()