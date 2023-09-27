def double_numbers(iterable):
    for i in iterable:
        print("[*] {} Double data generators!".format(i))
        yield i*2 # Lazy coding

# def double_numbers(iterable):
#     l=[]
#     for i in iterable:
#         print("[*] {} Double data generators!".format(i))
#         l.append(i*2)
#     return l

# def data():
#     print("[*] List data generators!")
#     return [1,2,3,4,5,6]

def data():
    l=[]
    for i in range(1,6):
        print("[*] {} List data generators!".format(i))
        l.append(i)
    return l

# Generating the data on-demand
for i in double_numbers(range(1,6)):
    print("Result of double data generators is {}".format(i))
print("\n")

# Iterating already available data
for i in data():
    print("Result of list data generators is {}".format(i))