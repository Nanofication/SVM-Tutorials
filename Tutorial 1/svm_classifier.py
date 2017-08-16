from matplotlib import pyplot as plt

from sklearn import datasets # Even after you use scikit learn, you don't know how to get the data
from sklearn import svm # I <3 SVM

# IN MACHINE LEARNING YOU NEED TO CONVERT EVERYTHING TO NUMBERS
# Convert all data to 0 or 1 or a range from -1 to +1

digits = datasets.load_digits()

# Gamma matters
clf = svm.SVC(gamma=0.001, C=100)

x, y = digits.data[:-1],digits.target[:-1] # This is data and targets all the way up to last number
clf.fit(x,y)

print "Prediction: ", clf.predict(digits.data[-1])

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
