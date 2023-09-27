var1=int(input("Enter a value 1: "))
var2=int(input("Enter a value 2: "))
if(var1>var2):
    print("I am {m} statement".format(m="if"))
    if(var1==var2):
        print("{} is equal to {}".format(var1,var2))
    if(var1!=var2):
        print("{} is not equal to {}".format(var1,var2))
else:
    print("I am {n} statement".format(n="else"))
