#importing array module
import array as ar
a=ar.array("i",[2, 4, 6, 8])
print(a)

#1D array
from array import*
a=array("i",[2, 4, 6, 8])
print(a)

#2D array
b=[[1, 2, 3, 4, 5],[6, 7, 8, 9]]
print(b)


#Add elements
import array as arr
num=arr.array("i",[1,2,3,4,5])
num[0]=0
print(num)

import array as arr
num=arr.array("i",[1,2,3,4,5])
num[2:5]=arr.array("i",[4,6,8])
print(num)


#Delete Elements
import array as arr
num=arr.array("i",[1,2,3,4,5])
del num[2]
print(num)

#Concatenation
import array as arr
a=arr.array('d',[1.0,2.0,3.0,4.0,5.0])
b=arr.array('d',[2.1,3.1])
c=arr.array('d')
c=a+b
print("C=",c)