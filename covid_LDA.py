import os 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import decomposition
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import random
random.seed(1)

def read_sample(file):
	sample = pd.read_csv(file, sep="\t", header=None).T 
	sample = sample.iloc[[1]]
	return sample

data_path = '/data7/wl/program/2022/covid/data/'
os.chdir(data_path)

sample = pd.DataFrame()
for dir in os.listdir(data_path):
	for file in os.listdir(dir):
		temp = read_sample(os.path.join(dir, file))
		temp["cat"]=os.listdir(data_path).index(dir)
		sample = sample.append(temp)
sample = sample.reset_index(drop=True)

x = sample.drop(['cat'], axis = 1)
y = sample["cat"]

plt.figure(figsize=(8, 8))
plt.plot(x)
plt.title("input")
plt.savefig(r"/data7/wl/program/2022/covid/input.png")
plt.show()


pca = decomposition.PCA()
pca.fit(x)

plt.figure(figsize=(8, 8))
plt.plot(pca.explained_variance_, 'k')
plt.title("explained variance")
plt.savefig(r"/data7/wl/program/2022/covid/pca.png")
plt.show()

colors=['red', 'blue', 'green']
x_pca = pca.transform(x)

#LDA
lda3cat = LinearDiscriminantAnalysis(n_components = 2)
x_lda = lda3cat.fit(x, y).transform(x)

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
for i in range(0, 3):
	plt.scatter(x_lda[y==i, 0], x_lda[y==i, 1], color=colors[i], label=os.listdir(data_path)[i])
plt.legend()
plt.title("LDA")

plt.subplot(2, 1, 2)
for i in range(0, 3):
	plt.scatter(x_pca[y==i, 0], x_pca[y==i, 1], color=colors[i], label=os.listdir(data_path)[i])
plt.legend()
plt.title("PCA")
plt.savefig(r"/data7/wl/program/2022/covid/LDA_PCA.png")
plt.show()