import pandas as pd 
from matplotlib import pyplot as plt 
from scipy.cluster import hierarchy
import numpy as np 

# Read in the dataset
# Drop any fields that are strings
# Only get the first 40 beacuase this dataset is big
df = pd.read_csv('pokemonW2.csv')
df = df.set_index('id')
del df.index.name 
df = df.drop(["type_1", "type_2", "species"], axis=1)
df = df.head(n=40)
print(df)

#Calculate the distance between each sample
Z = hierarchy.linkage(df, 'ward')

# Orientation our tree
hierarchy.dendrogram(Z, orientation="left", labels=df.index)

plt.show()