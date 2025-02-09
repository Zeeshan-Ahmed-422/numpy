import numpy as np
arr=np.matrix([[2,3,5,6],[6,8,9,4],[2,3,5,6],[6,8,9,4]])
tra=np.transpose(arr)
print(tra)

print()

print(arr.T)#shotcut of transpose
swap=np.swapaxes(arr,0,1)
print(swap)

print()

var2=np.matrix([[2,3],[4,5]])
print(var2)
print()
swa=np.swapaxes(var2,0,1)
print(swa)

var3=np.matrix([[2,3],[4,5]])
print()

z=np.linalg.inv(var3)
print(z)