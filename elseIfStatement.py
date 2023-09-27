var1=int(input("Enter a value 1: "))
var2=int(input("Enter a value 2: "))
if(var1>var2):
    print("I am {m} statement ".format(m="if"))
elif(var2>var1):
    print("I am {n} statement ".format(n="elif"))
else:
    print("I am {l} statement ".format(l="else"))