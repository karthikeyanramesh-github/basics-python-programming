import sys
# a=10
# b=[1,2,3,4,5]
# c=2
def divide(a,b):
    if(b==0):
        raise Exception("Cannot Divide by Zero!")
    return a/b
try:
    c=divide(99,9)
    print("Value of c is {}".format(c))
except NameError as ne:
    print("NameError Happened: {}".format(ne))
except IndexError as ie:
    print("IndexError Happened: {}".format(ie))
except Exception as e:
    print("Something else: {}".format(e))
    print("Error: {}".format(sys.exc_info()))
else:
    print("All Good!")
finally:
    print("Whatever the case is,I will Works!")