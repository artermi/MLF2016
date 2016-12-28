import random
import operator

class number:
    def __init__(self):
        self.x = random.uniform(-1,1) 
        self.y = 1 if self.x >= 0 else -1
        if random.random() < 0.2:
            self.y = -self.y
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
    def __lt__(self,other):
        return self.x < other.x

class hypo:
    def __init__(self,a,b,c):
        self.s = a
        self.th = b
        self.errate = c

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

class inout:
    def __init__(self,ein,eout):
        self.ein = ein
        self.eout = eout

def run_function():
    data = []
    for i in range(10):
        a = number()
        data.append(a)

    data.sort()
#    print_list(data)
    hp = find_hypo(data)
    return inout(hp.errate,0.5 - 0.3 * hp.s *(1 - abs(hp.th)))


def print_list(sth = []):
    for i in range(len(sth)):
        print(sth[i])


t_in = 0
t_out = 0
f_in = open('17.dat','w')
f_out = open('18.dat','w')
for i in range(5000):
    inout_i = run_function()
    f_in.write(str(inout_i.ein) + '\n')
    f_out.write(str(inout_i.eout) + '\n')
    t_in += inout_i.ein
    t_out += inout_i.eout

f_in.closed
f_out.closed

print('ein:',t_in/5000,'eout:',t_out/5000)
