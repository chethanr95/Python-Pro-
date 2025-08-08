###
def myfun(pri, roi) :
    int = ( pri * roi ) / 100
    print(f"int = {int}")


myfun(10000, roi=7.1)


###*args
def myfun1(*args, roi) :
    pri = 0
    for p in args: 
        pri += p
    int = ( pri * roi ) / 100     
    print(f"pri={pri}, roi={roi}, int={int}")
myfun1(10000, 5000, 12000, 3000, roi=7.1)    


###**kwargs
def myfun2(*args, **kwargs) :
    pri = roi = 0.0
    for p in args : 
        pri += p 
    for i, roi in kwargs.items() : 
        print(i,roi)
        int = ( pri * roi ) / 100
        print(f"pri={pri}, i={i}, roi={roi}, int={int}")

myfun2(10000, 5000, 3000, 12000, roi1=2.5, roi2=5, roi3=7.1)