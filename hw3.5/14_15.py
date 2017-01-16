import math as m
import operator
import numpy as np
from numpy import array as a
from numpy.linalg import inv

def sigmoid(s):
    return m.exp(s)/(1+m.exp(s))

def ridge_reg(Z,Y,la): 
    return  np.dot(np.dot(inv(a([[la,0,0],[0,la,0],[0,0,la]]) + np.dot(Z.transpose(),Z)), Z.transpose()),Y)


data = []
valu = []

for line in open('13.train','r'):
    x = a([1.0 for i in range(3)])
    for i in range(len(line.split() )- 1 ):
        x[i] = line.split()[i]
    valu.append(line.split()[-1])
    data.append(x)


for l in range(2,-11,-1):
    print(l,':')
    la = 10 ** l

    wreg = ridge_reg(a(data),a(valu,'d'),la)
 #   print(wreg)


    ein = 0
    i = 0
    for d in data:
        ein += 0 if np.dot(a(d),wreg) *int( valu[i]) > 0 else 1
        i += 1
    print ('ein',ein/len(data))

    err = 0
    N = 0
    for line in open('13.test','r'):
        x = a([1.0 for i in range(3)])
        for i in range(len(line.split())-1 ):
            x[i] = line.split()[i]
        er = 0 if np.dot(a(x),wreg) * int(line.split()[2]) > 0 else 1
        err += er
#    print(err)
        N += 1

    print('eout',err/N)
#print(wreg)
