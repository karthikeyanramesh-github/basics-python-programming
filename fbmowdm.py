def basic_mathematics_operation(a,b):
    p=a+b
    q=a-b
    r=a*b
    s=a/b
    return {
        "Addition":p,
        "Subraction":q,
        "Multiplication":r,
        "Division":s
    }
x=int(input("Enter Number 1: "))
y=int(input("Enter Number 2: "))
d=basic_mathematics_operation(x,y)
for i in d.keys():
    print("{} of {} and {} is {}".format(i,x,y,d[i]))
