from matplotlib import pyplot as plt

from sklearn import datasets # Even after you use scikit learn, you don't know how to get the data
from sklearn import svm # I <3 SVM

# IN MACHINE LEARNING YOU NEED TO CONVERT EVERYTHING TO NUMBERS
# Convert all data to 0 or 1 or a range from -1 to +1

digits = datasets.load_digits()

# Gamma matters (Isn't this learning rate?)
clf = svm.SVC(gamma=0.0001, C=100)
# What gamma does is to take steps to the global minima
# Gradient descent. You're trying to get down a mountain.
# What is the proper number of leap size to get to your answer as quickly as efficiently as possible

x, y = digits.data[:-10],digits.target[:-10] # This is data and targets all the way up to last number
clf.fit(x,y) # Fits a line to the numbers plotted on the graph
# Low number of variables, you can plot it. But if you see squiggly lines you're overfitting

print "Prediction: ", clf.predict(digits.data[-2])

plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()