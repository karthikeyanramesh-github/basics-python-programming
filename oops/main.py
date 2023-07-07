# import lib
# import lib.user as ls
# import image2ascii
# from lib.user import getuser
from lib.bike import Bike as bk
from lib.car import Car as cr
from lib.automobile import Automobile as am
from lib.bike import fm 

# print(lib.add(8,9))
# print(ls.getuser("Karthik"))
print("Oops Concept : main.py")
print("Bike Class")
print("---------------------------------------------")
x=bk("Bajaj Pulsar","150","TN90TR8954")
y=bk("KTM Duke","200","TN45KD87657")

x.batt=78
y.batt=67

x.start()
# call with object instance
x.battery()
y.start()
y.battery()

# call with class instance
bk.battery(x)
bk.battery(y)
print("Type --> {} ".format(bk.type))
# @classmethod

# @staticmethod
bk.anything()

bk.derive_max_speed()

fm("Function Method")

bk.bajaj("TN14T2578") #@classmethod
bk.tvs("TN14X6279") #@staticmethod

print(x.brand)
x.brand="yamaha"
print(x.brand)

# in-built del keyword 
del x.brand

a=bk("Bajaj Pulsar","150","TN90TR8954")
b=bk("KTM Duke","200","TN45KD87657")

print("type : {}".format(a.type))
a.type="noraml bikes"

#object is a instance of class
# call object instance does change type
print("after change type : {}".format(a.type))

# call class doesn't change type
print("type : {}".format(bk.type))

print("------------------------------------------------")

print("Car Class")
print("--------------------------------------------------")

z=cr("Rolls Royce","","TN90Y4598")
print(z.make)

z.start()

print("---------------------------------------------------")

print("Automobile Class")
print("---------------------------------------------------")

d=am("BMW","z1","TN34Y0099")
print("From Automobile ---> make : {}".format(d.brand))

p=bk.build_from_automobile(d)
p.start()
