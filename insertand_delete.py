import numpy as np
arr=np.array([2,34,5,6,7,8,8])
print(type(arr))
# v=np.insert(arr,(2,4),(0,12))
v=np.append(arr,7)
print(v)
var_1=np.array([[2,3,4],[5,6,7]])
v_1=np.insert(var_1,(0,1),0,axis=0)
v_1=np.append(var_1,[[3,6,7]],axis=0)
print(v_1)

#Delete

arr2=np.array([2,34,5,6,7,8,8])
d=np.delete(arr2,1)
print(d)

arr0 = np.array([[1, 2, 3], 
                [4, 5, 6]])

# Insert 99 at index 1 (column-wise)
new_arr = np.insert(arr0, 1, 99, axis=1)

print(new_arr)


