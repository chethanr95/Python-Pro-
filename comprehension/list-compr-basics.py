my_list = [1,2,3,4]
new_list = []

##without list_comprehension: 
#for n in my_list :
#    new_list.append(n*2)

##with list comprehension
##syntax: new_list = [new_item for item in list]    (or)  new_list = [n for n in list ]
#new_list = [n*2 for n in my_list]
#print(new_list)

##convert string to a list of chars with list comprehension:
##syntax: new_list = [n for n in string]
name="chethan r"
print(name)

chars_list = [n for n in name]
print(chars_list)

##conditional List Comprehension
#syntax: new_list = [new_item for item in list if condition] 
##(or)   new_list = [n for n in list if condition]
names = ["anu", "raaghu", "chandu", "chethu"]
print(names)
new_names = [name.upper() for name in names if len(name) > 3 ]
print(new_names)

#squares list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)
sqr_nums = [n*n for n in nums]
print(sqr_nums)

##filter out even numbers from the series of input
#input_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

input_nums = input("Enter list of numbers").split(",")
even_nums =[int(n) for n in input_nums if int(n) % 2 == 0]
print (even_nums)

