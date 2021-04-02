import train
import RN
import gest

def main():
    try:
        weight=open("weights.txt","r")
        for line in weight:
            gest.openW(train.layer1,line)
            gest.openW(train.layer2,line)
        weight.close()
    except IOError:
        gest.randomWeight(train.layer1.w,train.layer1.perc,train.layer1.dend)
        gest.randomWeight(train.layer2.w,train.layer2.perc,train.layer2.dend)


    #input
    train.layer1.m=[]
    for j in range(train.layer1.dend):
        a=int(input())
        train.layer1.m.append(a)

    #activate network
    RN.RN(train.layer1,train.layer2)

    #print output network
    train.layer2.y=gest.output(train.layer2.y)
    print("result=  " + str(train.layer2.y))

if __name__ == '__main__':
    main()
