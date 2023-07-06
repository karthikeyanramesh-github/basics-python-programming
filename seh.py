import sys
a = 10
b = [1,3,4,6,7,8]
c = 9
try:
    c = a+b[9]
    print("Sum of Two Numbers = {}".format(c))
except:
    print("Unexcepted Error: {}".format(sys.exc_info()[0]))

