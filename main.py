import train
import execute

'''
this is neural network formed by 2 layers. 
The first made of 9 percettrons with 8 dendrites (7 + bias) while second formed by 9 percettrons with 10 dendrites (9 + bias)
configure input file
configure oracle file
test this ANN
'''

command=[
    '  -train',
    '  -execute',
    '  -help',
    '  -exit'
]
def help():
    print('\nlist command\n')
    for i in command:
        print(i)
    print('\n\n')

def t():
    train.main()

def e():
    execute.main()

def main():
    while(1):
        cmd=input('input command:\n')
        if(cmd == 'train'):
            t()
        elif(cmd == 'execute'):
            e()
        elif(cmd == 'help'):
            help()
        elif(cmd == 'exit'):
            exit(1)

if __name__ == '__main__':
    main()