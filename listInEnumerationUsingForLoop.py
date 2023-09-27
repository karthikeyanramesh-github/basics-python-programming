lr=["Mohan","Lakshmanan","Priyanka","Moni","Mohana prasath","Ns mohan","Akash","Ramana","Santhoshini","Karthikeyan","Sachin","Kabil raj","Dinesh","Jacob paul"]
print(type(lr))
print(type(enumerate(lr)))
e=enumerate(lr)
for i in range(len(lr)):
    print(e.__next__())