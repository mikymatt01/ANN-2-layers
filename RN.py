import math

def weightedSum(w,m,dend,perc):#weighted sum every layer
    s=[]
    for i in range(perc):
        somma=0
        for j in range(dend):
            somma+=m[j]*w[i*dend+j]
        s.append(somma)
    return s

def actived(s):#activation function
    y=[]
    for somma in s:
        y.append(1/(1+math.exp(-somma)))
    return y

def Dactived(t):#derivative activation function
    res=1/(1+math.exp(-t))
    res=res*(1-res)
    return res

def map_in_out(y1):#map output layer 1 in input layer 2
    m2=[]
    m2.append(1)
    for i in y1:
        m2.append(i)
    return m2

def calibrate_outlayer(w,rate,y,d,m,perc,dend,s):#calibrate weights outside layer
    for i in range(perc):
        for j in range(dend):
            w[i*dend+j]+=rate*2*(d[i]-y[i])*m[j]*Dactived(s[i])
    return w

def calibrate_deeplayer(l1,rate,l2):#calibrate weights inside layer
    for i in range(l1.perc):
        d=0
        for k in range(l2.perc):
            d+=l2.w[k*l2.dend+i]*2*(l2.d[k]-l2.y[k])*Dactived(l2.s[k])
        for j in range(l1.dend):
            l1.w[i*l1.dend+j]+=rate*l1.m[j]*d*Dactived(l1.s[i])
    return l1.w

def RN(layer1,layer2):#neural network
    layer1.s=weightedSum(layer1.w,layer1.m,layer1.dend,layer1.perc)
    layer1.y=actived(layer1.s)

    layer2.m=map_in_out(layer1.y)

    layer2.s=weightedSum(layer2.w,layer2.m,layer2.dend,layer2.perc)
    layer2.y=actived(layer2.s)