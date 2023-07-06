lr=["mohan","lakshmanan","priyanka","moni","mohana prasath","mohan","akash","ramana","santhoshini","karthikeyan","sachin","kabil raj","dinesh","jacob paul"]
print(type(lr))
print(type(enumerate(lr)))
e=enumerate(lr)
for i in range(len(lr)):
    print(e.__next__())