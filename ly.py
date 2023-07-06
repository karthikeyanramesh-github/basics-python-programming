def double_numbers(iterable):
    for i in iterable:
        print("[*] {} Double Data Generators!".format(i))
        yield i*2 # Lazy Coding

# def double_numbers(iterable):
#     l=[]
#     for i in iterable:
#         print("[*] {} Double Data Generators!".format(i))
#         l.append(i*2)
#     return l

# def data():
#     print("[*] List Data Generators!")
#     return [1,2,3,4,5,6]

def data():
    l=[]
    for i in range(1,6):
        print("[*] {} List Data Generators!".format(i))
        l.append(i)
    return l

# Generating the Data On-Demand
for i in double_numbers(range(1,6)):
    print("---> Result of Double Data Generators is {}".format(i))
print("\n")

# Iterating Already Available Data
for i in data():
    print("---> Result of List Data Generators is {}".format(i))