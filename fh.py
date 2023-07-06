filename=input("Enter a Filename or Path to read: ")
f=open(filename,'r')
print(f.read())
f.close()