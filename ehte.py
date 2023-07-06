import sys
a=10
b=[1,2,3,4,5]
c=9
try:
    c=a+b[c]
    raise IOError("This is a Sample Error!")
    print("Value of c is {}".format(c))
except NameError as ne:
    print("NameError Happened: {}".format(ne))
except IndexError as ie:
    print("IndexError Happened: {}".format(ie))
except Exception as e:
    print("Something else: {}".format(e))
    print("Error: {}".format(sys.exc_info()[0]))
else:
    print("All Good!")
finally:
    print("Whatever the case is,I will Works!")