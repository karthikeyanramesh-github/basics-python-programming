num1=int(input("enter the value1: "))
num2=int(input("enter the value2: "))
# id() function look like a pointer or memory address
print("user input interger value in id() function --->")
print(id(num1))
print(id(num2))
# id() function for lists interger
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
print("lists value in id() function --->")
print(id(l1))
print(id(l2))
