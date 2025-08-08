class P() :
    pass

class C(P) :
    pass

print(issubclass(C,P))
print(issubclass(P,C))

o1 = P()

print(isinstance(o1,P))
print(isinstance(o1,C))
