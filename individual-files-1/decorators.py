print("BEGIN >")

def upper_decorator(func) : 
    def wrapper( val1, val2 ) :
        val1=val1.upper()
        val2=val2.upper()
        return func(val1, val2)
    return wrapper

@upper_decorator
def welcome(name1, name2) :
    return "Hello " + name1 + " ! Hai " + name2 + " !"

print(welcome("john", "doe"))
    