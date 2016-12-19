import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model #this allows us to preform the regression
data = np.loadtxt("my_data.txt")
#link for this data: www3.nccu.edu.tw/~hmlien/statistics/lecture/Linear%20Regression%20Example%20Data.pptx
xs = data[:,0] #our x-coordinate data, whatever it might be
ys = data[:,1] #our y-coordinate data
xs = np.array([xs]).T #this turns our x data into an array for processing
reg = linear_model.LinearRegression()

reg.fit(xs, ys) #trains the data
a = reg.coef_[0] #the slope of the line of best fit
b = reg.intercept_ #the y-intercept of the slope of the line of best fit
ablineValues = [] #this stores the new y-corrdates of the line of best fit
for i in xs:
    ablineValues.append(a*i[0]+b)
print "The slope is: ", a
print "The intercept is: ", b
prediction_value = input("Enter the x value for a prediction: ")
print reg.predict(prediction_value)
plt.scatter(xs, ys)
plt.plot(xs, ablineValues, 'r')
plt.show()
