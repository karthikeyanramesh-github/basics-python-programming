print("<---Iterables--->")
l=[1,2,3,4,5]
d={"r":"ramesh", "s":"suresh", "g":"ganesh", "d":"dinesh"}
for i in iter(d):
    print(i)
ld=iter(l)
print(next(ld))
print(next(ld))
print(next(ld))
print(next(ld))
print(next(ld))