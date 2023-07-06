import sys
def divide(a,b):
    if(b==0):
        raise ZeroDivisionError("Cannot Divide by Zero!")
    return a/b
try:
    c=divide(99,0)
    print("Value of c is {}".format(c))
except (NameError,IndexError,KeyError) as e:
    print("Error Happened: {}".format(e))
except ZeroDivisionError as zde:
    print("ZeroDivisionError: {}".format(zde))
else:
    print("All Good!")
finally:
    print("Whatever the case is,I will Works!")