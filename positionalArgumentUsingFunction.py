def add(a,*b):
    print(a)
    print(b)
    r=0
    r=r+a
    for i in b:
        r=r+i
    return r
print("Addition result: {}".format(add(1,2,3,4,5,6,7,8,9)))