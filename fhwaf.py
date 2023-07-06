while(1):
    filename=input("Enter a filename: ")
    f=open(filename,'w')
    f.write(input("Write Something.......\n"))
    while True:
        line = input()
        if line == "":
            break
        f.write(line + "\n")
    f=open(filename,'r')
    # print(f.read())
    op1=input("Do you want to Continue? Append the content in existing file ENTER (y:YES OR n:NO) ---> ")
    if(op1=='y'):
        f=open(filename,'a')
        f.write(input("Write Something in Your Existing File.......\n"))
        while True:
            line = input()
            if line == "":
                break
            f.write(line + "\n")
        f=open(filename,'r')
        print(f.read())
    else:
        break
    op2=input("Again do you want to write a file ENTER (y:YES OR n:NO): ---> ")
    if(op2=='n'):
        break
    f.close()
