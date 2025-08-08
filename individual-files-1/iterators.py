#iterator = object that has countable number of values
#         = iterate over values.
#         = implemented the iterator protocol eith __iter__() __next__() methods

mylist = ["one", "two", "three", "four"]
print(mylist)

itr = mylist.__iter__()

print(itr)

print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

