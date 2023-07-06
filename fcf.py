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
a,s,m,d=operation(99)
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
a,s,m,d=operation(99)
print("Addition = ",a(9))
print("Subraction = ",s(90))
print("Multiplication = ",m(8))
print("Division = ",d(9))