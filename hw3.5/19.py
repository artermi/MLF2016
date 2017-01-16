import math as m
import operator
import numpy as np
from numpy import array as a
from numpy.linalg import inv

def sigmoid(s):
    return m.exp(s)/(1+m.exp(s))

def ridge_reg(Z,Y,la): 
    return  np.dot(np.dot(inv(a([[la,0,0],[0,la,0],[0,0,la]]) + np.dot(Z.transpose(),Z)), Z.transpose()),Y)


def create_train_test(data,val,tr_data,tr_val,ts_data,ts_val,j):
    for i in range(len(data)):
        if i >= j*40 and i < (j+1) * 40:
            ts_data.append(data[i])
            ts_val.append(val[i])
        else:
            tr_data.append(data[i])
            tr_val.append(val[i])



tmp_data = []
tmp_valu = []

max_lamb = [0.0 for i in range(13)]


for line in open('13.train','r'):
    x = a([1.0 for i in range(3)])
    for i in range(len(line.split() )- 1 ):
        x[i] = line.split()[i]
    tmp_valu.append(line.split()[-1])
    tmp_data.append(x)

for j in range(5):
    data = []
    valu = []
    data_val = []
    valu_val = []
    create_train_test(tmp_data,tmp_valu,data,valu,data_val,valu_val,j)
#    print (j)

    for l in range(2,-11,-1):
 #       print(l,':')
        la = 10 ** l

        wreg = ridge_reg(a(data),a(valu,'d'),la)
     #   print(wreg)


        ein = 0
        i = 0
        for d in data:
            ein += 0 if np.dot(a(d),wreg) *int( valu[i]) > 0 else 1
            i += 1
#        print ('ein',ein/len(data))
    
        eva = 0
        i = 0
        for d in data_val:
            eva += 0 if np.dot(a(d),wreg) *int( valu_val[i]) > 0 else 1
            i += 1
#        print ('ecv',eva/len(data_val))


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

 #       print('eout',err/N)

#        if eva/len(data_val) > max_lamb[2 - l]:
        max_lamb[2 - l] += eva/len(data_val)

for m in range(len(max_lamb)):
    print(2 - m, max_lamb[m]/ 5)

#print(wreg)
