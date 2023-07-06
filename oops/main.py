# import lib
# import lib.user as ls
# import image2ascii
# from lib.user import getuser
from lib.bike import bike
# from lib.bike import fm 

# print(lib.add(8,9))
# print(ls.getuser("Karthik"))

x=bike("Bajaj Pulsar","150","TN90TR8954")
y=bike("KTM Duke","200","TN45KD87657")

x.batt=78
y.batt=67

x.start()
# call with object instance
x.battery()
y.start()
y.battery()

# call with class instance
bike.battery(x)
bike.battery(y)
print("Type --> {} ".format(bike.type))
# @classmethod
bike.types()

# @staticmethod
# bike.anything()

bike.derive_max_speed()

# fm("Function Method")




