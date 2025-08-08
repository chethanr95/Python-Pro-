file1 = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/list_comprehension/file1.txt"
file2 = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/list_comprehension/file2.txt"
#-------------
with open(file1) as f1 :
    file1_list = f1.readlines()


print(file1_list) #[1\n,2\n,3\n]

file1_list = [n.strip() for n in file1_list] 
print(file1_list)   #['1','2','3','4']

file1_list = [int(n) for n in file1_list]
print(file1_list)   #[1,2,3,4]
#------------
with open(file2) as f2 :
    file2_list = f2.readlines()

file2_list = [n.strip() for n in file2_list]
print(file2_list)    

file2_list = [int(n) for n in file2_list]
print(file2_list)

#--Print values of file1 also predsent in file2
common_list  = [n for n in file1_list if n in file2_list]
print(f"common_list={common_list}")

#contentes of f1 missin in f2
f1_only_list = [n for n in file1_list if n not in file2_list]
print(f"f1_only_list={f1_only_list}")