from sklearn import neural_network
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy
import matplotlib.pyplot as plt
data = datasets.load_digits()
print(data.keys())
plt.imshow(data.images[11],cmap=plt.cm.gray_r,interpolation = 'nearest')
plt.show()
