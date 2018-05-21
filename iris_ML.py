#!/usr/bin/python3

import time
import sklearn
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

#storing the data of the file in some variable 
iris = load_iris()

#taking description
fl_des=iris.DESCR

#taking flower names into a variable
fl_name = iris.target_names

#taking flower features into a variable
fl_features = iris.feature_names

#taking data into a variable
fl_data = iris.data

#taking target_values into a variable
fl_target = iris.target

#dividing the  50 data_values into 3 categories of flowers out of 150 
#for setosa flower
data_seto=fl_target[0:50]
d_seto=fl_data[0:50]

#for versicolor flower
data_versi=fl_target[50:100]
d_versi=fl_data[50:100]

#for virginica flower
data_virgi=fl_target[100:150]
d_virgi=fl_data[100:150]

#training the data_values by taking 49 values out of 50
train_seto=data_seto[0:49]
t_seto=d_seto[0:49]

train_versi=data_versi[0:49]
t_versi=d_versi[0:49]

train_virgi=data_virgi[0:49]
t_virgi=d_virgi[0:49]
#print("train is : ",train_virgi)
#print("t_versi is :",t_virgi)

#combining all three into one 
input_data=np.concatenate((t_seto,t_versi,t_virgi))
print("input data is : ",input_data)

#testing the data_values by taking 1-1 values for each
test_seto=data_seto[-1]
tes_seto=d_seto[-1]

test_versi=data_versi[-1]
tes_versi=d_versi[-1]

test_virgi=data_virgi[-1]
tes_virgi=d_virgi[-1]
print("test :",tes_virgi)

output_data=np.concatenate((train_seto,train_versi,train_virgi))
print("output data is : ",output_data)

#now loading the decision tree classifier
algo=tree.DecisionTreeClassifier()

#now fitting the values into the data
fit_data=algo.fit(input_data,output_data)


#predicting the values
predict=fit_data.predict((tes_seto,tes_versi,tes_virgi))
print("The predicted values are : ",predict)

plt.title("Graph between the flowers and dataset")
plt.xlabel("data")
plt.ylabel("features")
plt.scatter(t_seto,t_versi,color='g',label="spot",marker='*',s=170)
plt.scatter(t_versi,t_virgi,color='r',label="dot",marker='*',s=170)
plt.scatter(t_virgi,t_seto,color='c',label="star",marker='*',s=170)
plt.legend()
plt.show()




