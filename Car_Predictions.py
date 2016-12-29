from sklearn import tree
import numpy as np
import pydotplus
import graphviz


data = np.loadtxt("Car_Data.txt")

cars = [0, 1, 2, 3, 3, 0, 2]

clf = tree.DecisionTreeClassifier()
clf.fit(data, cars)

new_car = clf.predict([16.0, 8, 300.0, 115.0, 3500.0, 12.0, 70, 1])

accuratcy_score = clf.score(data, cars)

if new_car == 0:
    print "Chevrolet"

elif new_car == 1:
    print "Buick"

elif new_car == 2:
    print "plymouth"

elif new_car == 3:
    print "ford"

print "The accuracy is ", accuratcy_score

dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("car.pdf")
