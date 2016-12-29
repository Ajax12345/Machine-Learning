from sklearn import tree
import numpy as np
import pydotplus
import graphviz

data = np.loadtxt("my_data.txt") #data from http://www.math.uah.edu/stat/data/Fisher.html

flower_type = data[:,0]
flower_data = np.loadtxt("my_data.txt", usecols=[1,2,3,4])

clf = tree.DecisionTreeClassifier()
clf.fit(flower_data, flower_type)
new_flower = clf.predict([3, 15, 45, 36])
print clf.score(flower_data, flower_type)
if new_flower == 0:
    print "Setosa"

elif new_flower == 1:
    print "Verginica"

elif new_flower == 2:
    print "Versicolor"

else:
    print "unkown"

dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("iris.pdf")
