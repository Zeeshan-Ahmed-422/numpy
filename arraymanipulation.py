import numpy as np
a=np.arange(0,27)
print(a)
# # reshape threedim
# # b=np.reshape(a,(3,3,3))
# # print(b)
print(a.shape)
# # print(b.shape)
# # print(np.reshape(a,(3,3,3),order="f"))
a.reshape((3,3,3),order="f")
print(a)
# # resize
print(np.resize(a,(6,6)))
a.resize((6,6))
print(a)
# help(np.reshape)


# arrayflattening



a=np.array([[[23,44,55],[3,7,8]],[[34,89,9],[78,6,9]]])


# x=np.flatten(a,order="c")
b=a.flatten()
print(b)

# arrayshuffling

z=np.array([[[23,44,55],[3,7,8]],[[34,89,9],[78,6,9]]])
s=np.random.shuffle(z)
print(s)
for i in range(1,5):
    
     t=int(input("write no"))
     
# print(t)



