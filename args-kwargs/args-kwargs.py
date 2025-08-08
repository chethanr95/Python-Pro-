def sum(*args) :
    print("*args, Unlimited Positional args ,type=tuple")
    total = 0
    print(type(args))
    for n in args :
        total += n
    print(f"total={total}")    

sum(2,4,6,8,10,11,12,13,14,15)    
sum(1,3,5,7,9)

def result(n,**kwargs) :
    print("**kwargs, Unlimited keyword args, type= dictionary")
    n1 = n
    #n2 = kwargs["add"]
    n2 = kwargs.get("add")
       
    print(f"n2={n2}") 

result(7, add=101)   
result(7) 

