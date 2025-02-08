import numpy as np
ar=np.array([1,3,4,6,8])
print(ar)
print()
for i in ar:
    print(i)
# print(ar[0:4:1])
ar1=np.array([[2,3,4],[6,7,4]])
print(ar1)
for j in ar1:
    print(j)
    for k in j:
        print(k)
ar2=np.array([[[2,4,5],[5,9,0]]])        
for l in ar2:
    print(l)
    for x in l:
        print(x)
        for m in x:
            print(m)
ar2=np.array([[[2,4,5],[5,9,0]]])  
for v in np.nditer(ar2,flags=['buffered'],op_dtypes="S"):
    print(v)
ar3=np.array([[[2,4,5],[5,9,0]]])  
for v,p in np.ndenumerate(ar3):
    print(v,p)  


            