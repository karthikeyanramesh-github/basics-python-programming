def double_numbers(iterable):
    for i in iterable:
        print("[*] {} Double data generators!".format(i))
        yield i*2 
i=double_numbers(range(1,6))
k=next(i)
while k:
    print("Result of double data generators is {}".format(k))
    try:
        k=next(i)
    except:
        break