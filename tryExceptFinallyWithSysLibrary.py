import sys
a=10
b=[1,2,3,4,5]
c=6
try:
    c=a+b[c]
except NameError as ne:
    print("NameError happened: {}".format(ne))
except IndexError as ie:
    print("IndexError happened: {}".format(ie))
else:
    print("All good!")
finally:
    print("Whatever the case is,I will works!")