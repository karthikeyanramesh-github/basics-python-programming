def operation(x):
    def add(y):
        return x+y
    def sub(y):
        return x-y
    def mul(y):
        return x*y
    def div(y):
        return x/y
    return (add,sub,mul,div)
a,s,m,d=operation(1000)
l=[100,200,300,400]
print(list(map(a,l)))