# importing the decision tree library within scikit-learn

from sklearn import tree

# creating our data randomly giving 3 different features as a list of list
# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
     [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# creating the labels as strings
y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
# le's define a variable to store our decision tree model
# clf == short for classifier
clf = tree.DecisionTreeClassifier()

# train our dataset
clf = clf.fit(X, y)

# predict our gender and tested
pred = clf.predict([[181, 80, 44]])

print(pred)

