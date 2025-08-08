#generator = a function which returns an iterator object.
# = functin with atleast one yield expression
#yield is used in generator function instead of return because : 
#yield will retain the state of the function and in the next call of this generator functoin it will resume from the retained state. 

months = 12
emi = 0
def generator_func() : 
    global emi
    print("begin")
    yield emi
    print("resume")
    emi += 1


term = generator_func()    
print(type(term))
for t in term : 
    print(t)

term = generator_func()    
for t in term : 
    print(t)    

for e in range(11) :
    term = generator_func()    
    for t in term : 
        print(t)    
