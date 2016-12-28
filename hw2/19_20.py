import random
import operator

class number:
    def __init__(self):
        self.x = random.uniform(-1,1) 
        self.y = 1 if self.x >= 0 else -1
        if random.random() < 0.2:
            self.y = -self.y
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __lt__(self,other):
        return self.x < other.x

class hypo:
    def __init__(self,a,b,c):
        self.s = a
        self.th = b
        self.errate = c
    def __str__(self):
        return str(self.s) + ' ' + str(self.th) + ' ' + str(self.errate)
    def __lt__(self,other):
        return self.errate < other.errate

def find_hypo(data = []):
    trt = hypo(0,0,1)
    theta = [-1]
    for i in range(len(data)):
        theta.append(data[i].x)
    theta.append(1)

    for i in range(len(data) + 1):
        tmp = hypo(1, (theta[i] + theta[i+1])/2  ,1)
        count_error(tmp, data)
        if tmp.errate < trt.errate:
            trt = tmp
    
    for i in range(len(data) + 1):
        tmp = hypo(-1, (theta[i] + theta[i+1])/2  ,1)
        count_error(tmp, data)
        if tmp.errate < trt.errate:
            trt = tmp
    return trt

def count_error(hyp,dat = []):
    error = 0
    for i in range(len(dat)):
        sign = 1 if (dat[i].x - hyp.th) > 0 else -1
        if hyp.s * sign != dat[i].y:
            error += 1
    hyp.errate = error/len(dat)
    return hyp.errate

class inout:
    def __init__(self,ein,eout):
        self.ein = ein
        self.eout = eout

def run_function(data = []):
    data.sort()
    hp = find_hypo(data)
#    print(hp.s,hp.th)
    return hp 


data = [[]for i in range(9)]

for line in open('train', 'r'):
    for i in range(len(line.split()) - 1):
        data[i].append( number(float(line.split()[i]),int(line.split()[-1])) )


class hp_di:
    def __init__(self,hp,di):
        self.hp = hp
        self.di = di

best = hp_di(hypo(0,0,2),-1)

for i in range(len(data)):
    tmp =  hp_di(run_function(data[i]),i)
    best = tmp if tmp.hp < best.hp else best

print('the best hypo is:',best.hp,'dimenstion is:', (best.di + 1))

test = []
for line in open('test','r'):
    test.append(number(float (line.split()[best.di]), int(line.split()[-1])))

print('error rate:',count_error(best.hp,test))
