#support vector machine
from sklearn import svm
import numpy as np

data = np.loadtxt('my_new_data.txt')
result = [8, 2, 4, 7, 7, 11, 7, 11, 9, 7, 7, 7, 7, 7, 8, 7, 8, 8, 11, 7, 7, 9, 7, 9, 7, 9, 7, 9, 7]
clf = svm.SVC()
clf.fit(data, result)

the_new_play = clf.predict([0, 0, 1])
print clf.score(data, result)

if the_new_play == 1:
    print "Cover one"

elif the_new_play == 2:
    print "Cover 2"

elif the_new_play == 3:
    print "All out blitz"

elif the_new_play == 4:
    print " safetly blitz"

elif the_new_play == 5:
    print "Cover 3"

elif the_new_play == 6:
    print "rush"

elif the_new_play == 7:
    print "4-3"

elif the_new_play == 8:
    print "3-4"

elif the_new_play == 9:
    print "flex"

elif the_new_play == 10:
    print "zone blitz"

elif the_new_play == 11:
    print "46"
