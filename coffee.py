#User customer order Menu dictionary
MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18
        },
        "cost" : 1.0
    },
    "latte" : {
        "ingredients" :{
            "water" : 200,
            "milk" : 150,
            "coffee" : 24
        },
        "cost" : 2.0
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24

        },
        "cost" : 3.0
    }
}

#Machine Profit amount
profit = 0

#Machine resources
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}


#Manchine off or on
is_off = False

#User selection from the menu
order = "NONE"


#prompt until user enter valid value
def prompt_for_order() :
    
    selection = ""
    
    while selection not in MENU and selection != "off" and selection != "report" :
        selection = input("What would you like ? (espresso/latte/cappuccino) : ")
        selection = selection.lower()
    
    return selection


#Machine is on unless ordered off
def check_turn_off() :
    
    if order == "off" :
    
        print("Machine Turn Off")
        return "False"


#user order is NONE unless not_ordered    
def not_ordered() :
   
    if order == "NONE" :
        return True
   
    else :
        return False


#Print report of the current machine resources
def print_report() :

    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {profit}")


#check current Machine resources enough to the order requirement
def check_resources() : 

    having_res=False

    for res in MENU[order]["ingredients"] :
        #print (f"required: {MENU[order]["ingredients"][res]}")
        #print (f"existing: {resources[res]}")
        if MENU[order]["ingredients"][res] <= resources[res] :
            having_res = True
        
        else :
            print(f"{res} is out of Stock")
            having_res = False
            return having_res
        
    #print("All resources sufficient to continue")    
    return having_res #obvious always only True value here 


#process coins
def process_coins() :
    
    insert_coins = float(input("Insert required coins: "))

    if insert_coins > MENU[order]["cost"] :
        change = insert_coins - MENU[order]["cost"]
        print(f"Collect your change {change}")
        return True
    
    elif insert_coins == MENU[order]["cost"] :
        change = 0
        print(f"Exact money!")
        return True

    elif insert_coins < MENU[order]["cost"] :
        change = MENU[order]["cost"] - insert_coins
        print(f" Refeunded. Require {change} more money")
        return False


#Ready to coffee
def trigger_coffee() :
    
    print(f"All Set! Your coffee {order} is in the making")
    
    def update_resources() :
        
        global resources
        for res in MENU[order]["ingredients"] :
            resources[res] -= MENU[order]["ingredients"][res]

    def update_profit() :

        global profit
        profit += MENU[order]["cost"]

    update_resources()
    update_profit()
    
    print(f"\nEnjoy your {order}. Happy to Serve you :)\n")


#Main , Start of Program

while not_ordered() and not is_off:

    order = prompt_for_order()
    #print(f"You've ordered: {order}")
    is_off = check_turn_off()
    
    
    if order == "report" :
        print_report()
    
    elif order == "off" :
        is_off = True
    
    else:
        if check_resources() :

            if process_coins() :
                
                trigger_coffee()         
        
        else : 
            
            print("Top Up resources and Restart")  
            is_off = True
            print_report()
        
            
    order = "NONE"

#End of Program
