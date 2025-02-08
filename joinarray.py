import numpy as np
var=np.array([2,3,6])
var1=np.array([3,6,8])
a=np.concatenate((var1,var))
print(a)

v=np.array([[2,3,6],[5,7,8]])
v1=np.array([[3,6,8],[2,5,9]])
b=np.concatenate((v1,v),axis=0)
print(b)
var_1=np.array([[1,3,4],[6,8,9]])
var_2=np.array([[1,5,7],[1,0,1]])
c=np.stack((var_1,var_2),axis=1)
print(c)
d=np.hstack((var_1,var_2))#along row for colum vstack for height dstack
print(d)
e=np.vstack((var_1,var_2))#along row for colum vstack for height dstack
print(e)