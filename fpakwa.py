def keywordargs(*pargs,**kwargs):
    print(pargs)
    print(kwargs)
    return (pargs,kwargs)
keywordargs(1,2,3,a=1,b=2,c=3,d=4,e=5,f=6)