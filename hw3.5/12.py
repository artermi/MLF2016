import math as m
import operator
import numpy as np
from numpy import array as a

def sigmoid(s):
    return m.exp(s)/(1+m.exp(s))

eta = 0.001
T = 2000

def DE_in(data,w,y):
    de_in = a([0.0 for i in range(21)])
    i = 0
    for dat in data:
        de_in += sigmoid(- np.dot(dat,w) * y[i] ) * (-1 * y[i] * dat)

#    print de_in
    return de_in / len(data)

def error(x,w,y):
    return 1 if  y * np.dot(x,w) < 0 else 0
#    return  m.log(1 + m.exp(-np.dot(x[1:],w) * x[0]))
        
def SGD(dat,w,y):
    return sigmoid(- np.dot(dat,w) * y ) * (y * dat)

data = []
value = []
for line in open('11.train','r'):
    x = a([1.0 for i in range(21)])
    for i in range(len(line.split())-1 ):
        x[ i + 1] = line.split()[i]
    value.append(int(line.split()[-1]))
    data.append(x)


w = a([0] * 21)


for i in range(T):
    grad = SGD(data[i % len(data)],w,value[i%len(data)])
    w = w + eta * grad

err = 0.0
N = 0

for line in open('11.test','r'):
    x = a([1.0 for i in range(21)])
    for i in range(len(line.split() )-1 ):
        x[i + 1] = line.split()[i]
    vout = int (line.split()[-1])
    err += error(x,w,vout)
#    print(err)
    N += 1

print(err/N)
print(w)
