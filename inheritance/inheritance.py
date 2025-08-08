class Animal :
    
    def __init__(self) :
        self.eyes = 2
    
    def breathe(self) :
        print("inhale, exhale")

class Fish(Animal) :

    def __init__(self) :
        self.eyes = 3
        super().__init__()
    
    def breathe(self) :
        super().breathe()
        print("under water")
    
fish1 = Fish()
print(fish1.eyes)
fish1.breathe()
