import numpy as np
var=np.array([[1,2,4],[4,5,5]])
print(var )

print(var.shape)
var1 =np.array([1,2,3],ndmin=2)
print(var1)
print()
print(var1.shape)
#reshape
var2=np.array([1,2,3,4,5,6,1,2,3])
print(var2)
x=var2.reshape(3,3)
print(x)
print(x.ndim)

var3=np.array([1,2,3,4,5,6,1,2,])
print(var3)
x1=var3.reshape(2,2,2)
print(x1)
print(x1.ndim)
one=x1.reshape(-1)
print(one)
