#syntax of open command
#open("file_name", mode="r/w/a") #when mode argument not passed, default mode is"r"

my_file = "sample_file.txt"

#===================
#(1)WRITE . #create a new file 

#method 1 : with close() 
file_h = open(my_file, mode = "w")
file_h.write("line1.\nline2.\n")
file_h.close()

#method 2: without close(), y with open as file_h :
with open(my_file, mode="w") as file_h :
    file_h.write("LINE1.\nLINE2.\n")

#===================
#READ

#METHOD 1 : with close and default mode
file_h = open(my_file)        
contents = file_h.read()
print("A")
print(contents)

#Method 2 : with close and mode="r"
file_h = open(my_file, mode="r" )
contents = file_h.read()
print("B")
print(contents)

#Method 3: with as . default mode :
with open(my_file) as file_h :
    contents = file_h.read()
    print("C")
    print(contents)

#Method 4 : with as, mode="r"
with open(my_file, mode = "r") as file_h :
    contents = file_h.read()
    print("D")
    print(contents)
#===================
#APPEND

#Method 1 : with close
file_h = open(my_file, mode="a")
file_h.write("Line3.\n")
file_h.close()

#Method 2 : with as 
with open(my_file, mode="a") as file_h :
    file_h.write("Line4.\n")

#methods of file hadler:
# write()    
# read()
# readline()        
# readlines()

#readline() & readlines() 
with open(my_file, mode="r") as file_h :
    print("---")
    print(file_h.readline())    #Line1.

with open(my_file, mode="r") as file_h :
    print("===")
    print(file_h.readlines())