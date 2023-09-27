import copy
l=[1,2,3,[1,2,3,5],5,6,7,8,9,10]
u=copy.deepcopy(l)
for i in range(0,len(l)):
    print("#{} : data(l)->{} id->{}".format(i,u[i],id(u[i])))
    print("#{} : data-(d)>{} id->{}".format(i,l[i],id(l[i])))
