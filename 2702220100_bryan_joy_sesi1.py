# -*- coding: utf-8 -*-
"""2702220100-Bryan Joy-Lab01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ooInwEBTvn6dVRFSxBNfZlfx1o294n0k
"""

import time
print (time.ctime())

x = 1
y = 3
print (x,y)

x = x + 1
x

import numpy as np

x = np.array([3,1,4,3])
x

x = np.array([1,4,3])
y = np.array([2,5,7])
print(x)
print(y)

y = np.array([[1,4,3],[2,9,8]])
y

def a(a,b,c,d):

    x = a+b+c+d

    return x

a(1,2,3,5)

help(a)

def z(temp,dt):
  if temp < dt:
    status = 'Hot'
  elif temp > dt:
    status = 'Cold'
  else :
    status = 'Medium'
  return status

status = z(100,70)
print(status)

x = 1
if x>1 and x<2:
  y = 2
elif x>2 and x<4:
  y = 10
else:
  y = 'Error'

print(y)