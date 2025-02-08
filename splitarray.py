import numpy as np
var=np.array([3,5,7,2,8])
print(var)
print()
ar=np.array_split(var,3)
# print(ar)
# print(type(ar))
# print(ar[0])

var=np.array([[3,5],[7,2],[2,8]])
a=np.array_split(var,3,axis=0)
print(a)
