import numpy as np
var=np.array([2,5,7,3])
# var[1]=3
co=var.copy()
var[1]=3
print()
x=var.view()
print(x)
print(co)
# var1=np.array([3,9,5])
# x=var1.view()
# print(x)