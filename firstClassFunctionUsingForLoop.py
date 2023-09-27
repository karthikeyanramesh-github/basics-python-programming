def operation(x):
    def add(y):
        return x+y
    return add
a=operation(1000)
l=[100,200,300,400]
for v in l:
    print("Addition = ",a(v))