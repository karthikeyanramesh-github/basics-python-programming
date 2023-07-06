x=5
def set_x(num):
    x=num
    print("when calling function x value = ",x)
def set_global_x(num):
    global x
    print("x is assign a global value inside the function x = ",x)
    x=num
    print("when calling a function x value = ",x)

print("current x value = ",x)
set_x(99)
set_global_x(1000)
