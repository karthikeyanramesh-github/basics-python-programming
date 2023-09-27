def operation(x):
    def add(y):
        return lambda y: y+x
    return add
a=operation()
l=[100,200,300,400]
print(list(map(lambda y:y+40,l)))