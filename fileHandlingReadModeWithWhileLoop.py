filename=input("Enter a filename or path to read: ")
f=open(filename,'r')
line=f.readline()
i=1
while(line):
    print(line,end='')
    # print(line.split(','))
    if(i%1000==0):
        op=input("Do you want to read more? ENTER (y:YES OR n:NO) ---> ")
        if(op=='n'):
            print("Exiting...")
            break
    i=i+1
    line=f.readline()
f.close()
