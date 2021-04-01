import RN
import gest
import progressbar

class layer1:
    w=[]
    s=[]
    y=[]
    m=[]
    dend=8
    perc=9

class layer2:
    w=[]
    s=[]
    y=[]
    d=[]
    m=[]
    dend=9+1
    perc=9

rate=0.1
cicli=2000

def main():
    try:
        weight=open("weights.txt","r")
        for line in weight:
            gest.openW(layer1,line)
            gest.openW(layer2,line)
        weight.close()
    except IOError:
        gest.randomWeight(layer1.w,layer1.perc,layer1.dend)
        gest.randomWeight(layer2.w,layer2.perc,layer2.dend)

    weight=open("weights.txt","w")

    for i in progressbar.progressbar(range(cicli)):
        init=open("input.txt","r")
        oracle=open("oracle.txt","r")
        for line in init:
            
            #input e output
            layer1.m=gest.read(line)
            layer2.d=gest.read(oracle.readline())
            
            #activate network
            RN.RN(layer1,layer2)
            
            #calibrate weights layer 2
            layer2.w=RN.calibrate_outlayer(layer2.w,rate,layer2.y,layer2.d,layer2.m,layer2.perc,layer2.dend,layer2.s)
            
            #calibrate weights layer 1
            layer1.w=RN.calibrate_deeplayer(layer1,rate,layer2)

            if(i==cicli-2):
                print("input=   " + str(layer1.m))
                layer2.y=gest.output(layer2.y)
                print("goal=    " + str(layer2.d))
                print("result=  " + str(layer2.y))
                print("\n")

        init.close()
        oracle.close()

    #saved weights 
    gest.write(weight,layer1.w,layer1.dend,layer1.perc)
    gest.write(weight,layer2.w,layer2.dend,layer2.perc)

if __name__ == "__main__":
    main()