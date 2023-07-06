def double_numbers(iterable):
    for i in iterable:
        print("[*] {} Double Data Generators!".format(i))
        yield i*2 
i=double_numbers(range(1,6))
k=next(i)
while k:
    print("---> Result of Double Data Generators is {}".format(k))
    try:
        k=next(i)
    except:
        break