def basic_mathematics_operation_keyword_arguments(a,b):
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
d=basic_mathematics_operation_keyword_arguments(b=x,a=y) # keyword arguments
for i in d.keys():
    print("{} of {} and {} is {}".format(i,y,x,d[i]))
