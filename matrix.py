import numpy as np
mat=np.matrix([[1,2],[4,5]])
mat1=np.matrix([[1,2],[4,5]])
m=mat*mat1
print(m)
# print(mat)
print(mat.dot(mat1))
print(type(mat))


mt=np.array([[1,2],[4,5]])
mt1=np.array([[1,2],[4,5]])
n=mt+mt1
x=mt*mt1
print(np.dot(mt,mt1))
print(x)
print(n)
print(type(mt))