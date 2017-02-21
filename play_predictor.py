import numpy as np
from sklearn import svm
#decision tree

result = [5, 1, 5, 1, 3, 4, 5, 5, 4, 1, 2, 5, 1, 3, 3, 1, 4, 1, 1, 4, 5, 3, 3, 3, 4, 3]
data = np.loadtxt('my_new_data.txt')


clf = svm.SVC()
clf.fit(data, result)

the_new_play = clf.predict([0, 0, 1, 0])
if the_new_play == 1:
    print "Run"

elif the_new_play == 2:
    print "flip"

elif the_new_play == 3:
    print "short pass"

elif the_new_play == 4:
    print "medium pass"

elif the_new_play == 5:
    print "long pass"


print clf.score(data, result) #need to add the down
