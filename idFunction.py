num1=int(input("Enter the value1: "))
num2=int(input("Enter the value2: "))
# id() function look like a pointer or memory address
print("User input integer value in id() function")
print(id(num1))
print(id(num2))
# id() function for lists integer
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
print("Lists value in id() function")
print(id(l1))
print(id(l2))
