import math as m
import operator
import numpy as np
from numpy import array as a

def sigmoid(s):
    return m.exp(s)/(1+m.exp(s))

eta = 0.001
T = 2000

def DE_in(data,w):
    de_in = a([0.0 for i in range(20)])
    for dat in data:
        de_in += sigmoid(- np.dot(dat[1:],w) * dat[0] ) * (-1 * (dat[0]) * dat[1:])
#    print de_in
    return de_in / len(data)

def SGD(dat,w):
    return sigmoid(- np.dot(dat[1:],w) * dat[0] ) * ((dat[0]) * dat[1:])
    

def error(x,w):
    return 1 if  x[0] * np.dot(x[1:],w) < 0 else 0
#    return  m.log(1 + m.exp(-np.dot(x[1:],w) * x[0]))
        

data = []

for line in open('11.train','r'):
    x = a([0.0 for i in range(21)])
    for i in range(len(line.split() ) ):
        x[(i + 1)% 21] = line.split()[i]
    data.append(x)


w = a([0] * 20)

for i in range(T):
    grad = SGD(data[i % len(data)],w)
    w = w + eta * grad


err = 0.0
N = 0
for line in open('11.test','r'):
    x = a([0.0 for i in range(21)])
    for i in range(len(line.split() ) ):
        x[(i + 1)% 21] = line.split()[i]
    err += error(x,w)
#    print(err)
    N += 1

print(err/N)
print(w)
