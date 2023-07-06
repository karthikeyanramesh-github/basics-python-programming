import sys
a=10
b=[1,2,3,4,5]
c=6
try:
    c=a+b[c]
except NameError as ne:
    print("NameError Happened: {}".format(ne))
except IndexError as ie:
    print("IndexError Happened: {}".format(ie))
else:
    print("All Good!")
finally:
    print("Whatever the case is,I will Works!")