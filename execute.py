import train
import RN
import gest

def main():
    gest.openW(train.layer1,train.layer2)

    #fase lettura input e output desiderato
    train.layer1.m=[]
    for j in range(train.layer1.dend):
        a=int(input())
        train.layer1.m.append(a)

    #attivazione rete neurale
    RN.RN(train.layer1,train.layer2)

    #print output network
    train.layer2.y=gest.output(train.layer2.y)
    print("result=  " + str(train.layer2.y))

if __name__ == '__main__':
    main()