
mylist = [35, 30, 45, 10, 20, 15, 40, 25, 50]
even = lambda n : n % 2 == 0
even_filter = filter(even, mylist)
print(type(even_filter))
for n in even_filter :
    print(n)