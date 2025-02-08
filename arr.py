import numpy as np
# list1=[20,40.7,30,50]
# array1=np.array(list1,dtype='U16')
# print(array1)
# # type(array1)
# list2=[[20,40.7,30],[23,67,90],[23,87,67]]
# array2=np.array(list2,dtype=int)
# print(array2)
# array3=np.arange(23,30)
# print(array3)
# array4=np.arange(23,32).reshape((3,3))
# print(array4)
# array5=np.arange(11,17).reshape((2,3))
# print(array5)
# array6=np.ones((5,7))
# print(array6)
# l=[]
# for i in range(1,5):
#     inp=int (input("enter"))
#     l.append(inp)
# x=np.array(l)
# print(x.ndim)    
# a3=np.array([[[2,4,6],[1,2,5],[2,8,9]]])
# print(a3)
# print(a3.ndim)
# arn=np.array([1,2,3],ndmin=10)
# print(arn)
# print(arn.ndim)
# array_zeroes = np.zeros((2,4))  # Shape (2,2,2,2,2,2,2,2,2,2)
# print(array_zeroes)
# print(array_zeroes.ndim)
array_ones=np.ones((2,3,4))
print(array_ones)
arr_emp=np.empty((2,2))
print(arr_emp)
ar_rng=np.arange(2,7)
print(ar_rng)
# diagonal
ar_dia=np.eye(7)
print(ar_dia)
ar_dia=np.eye(2,3)
print(ar_dia)
# linspace
ar_lin=np.linspace(0,10,5)
print(ar_lin)
# random
var=np.random.rand(4,5)  #0 to 1
print(var)
var1=np.random.randn(4)   #negative also
print(var1)
var2=np.random.ranf(5)# 0 to 1.0 [o ,1) 1 not included
print(var2)
var3=np.random.randint(1,10,5)
print(var3)