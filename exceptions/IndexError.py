fruits = ['apple', 'orange', 'mango']

def make_pie(index) :
    try :
        fruit = fruits[index]
    except : 
        print("Fruit PIE")        
    else :    
        print(fruit + " Pie")


make_pie(2)

make_pie(3)