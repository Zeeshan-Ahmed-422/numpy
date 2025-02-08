import numpy as np
a=np.array([2,3,4])
b=np.array([8,3,4])
c=a+b
d=np.add(a,3) #two methods are there to add
print(c.transpose())
print(d)  
# minus plus ultiply divide same//
print(c)
z=np.array([[2,3,4],[23,54,5]])
y=np.array([[2,3],[4,23],[54,5]])
x=z@y  
z1=np.array([[2,3,4],[23,54,5]])
y1=np.array([[2,3,4],[12,4,7]])
w=z1+y1
print(w)  

print(x)
print(z.transpose())
q=np.array([[[2,3,4],[23,54,7]],[[2,5,7],[23,7,89]]])
w=np.array([[[2,3,4],[23,54,7]],[[2,5,7],[23,7,89]]])
e=q//w
print(e)  
dq=np.array([1,2,4,6])
recpr=np.reciprocal(dq)
print(recpr) 
vars=np.array([2,2,4,6,8,1,9,1])
print("sqrt",np.sqrt(vars))
print("minimum ",np.max(vars))
print("max space ",np.argmax(vars))
 
