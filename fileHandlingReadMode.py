filename=input("Enter a filename or path to read: ")
f=open(filename,'r')
i=0
while(i<5):
    print(f.readline(),end='')
    i=i+1
f.close()