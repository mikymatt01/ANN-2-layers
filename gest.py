import random

random.seed(1)

def write(file,w,dend,perc):
    for i in range(perc):
        for j in range(dend):
            file.write(str(w[i*dend+j]))
            file.write("\n")

def randomWeight(w,perc,dend):#genera pesi random per ogni livello
    for i in range(perc):
        for j in range(dend):
            w.append(random.random())

def openW(layer,line):
    if(len(layer.w)<layer.dend*layer.perc):
        layer.w.append(read(line)[0])

def read(line):
    numbers = []
    for word in line.split():
        try:
            numbers.append(float(word))
        except:
            print("error")
    return numbers

def output(d):
    res=[]
    for i in d:
        if i >=0.5:
            i=1.0
        else:
            i=0.0
        res.append(i)
    return res