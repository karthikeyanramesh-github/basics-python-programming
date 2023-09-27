def basic_mathematics_operation(a,b):
    p=a+b
    q=a-b
    r=a*b
    s=a/b
    return (p,q,r,s)
x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
p,q,r,s=basic_mathematics_operation(x,y)
print("Addition of {} and {} is {}".format(x,y,p))
print("Subraction of {} and {} is {}".format(x,y,q))
print("Multiplication of {} and {} is {}".format(x,y,r))
print("Division of {} and {} is {}".format(x,y,s))