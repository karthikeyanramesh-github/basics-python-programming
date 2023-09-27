l=[1,2,3,4,5,6,7,8,9,10]
u=l[::1]
# u=l.copy()
for i in range(0,len(l)):
    print("#{} : Data(l): {} id: {}".format(i,u[i],id(u[i])))
    print("#{} : Data(u): {} id: {}".format(i,l[i],id(l[i])))
