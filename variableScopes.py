x=5
def set_x(num):
    x=num
    print("When calling function x value = ",x)
def set_global_x(num):
    global x
    print("Value = {} is assign a global value inside the function {} = ".format(x))
    x=num
    print("When calling a function x value = ",x)

print("Current x({}) value = ".format(x))
set_x(99)
set_global_x(1000)
