#slicing examples
#syntax=   my_list[start_index, upto_index: increment]
#start_index = inclusive    #mandatory, empty = from 0 index inclusive
#upto_index = exclusive     #mandatory, empty = upto last index inclusive
#increment = 2 = alternate # not mandatort

piano_list = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_list[:5])   # a b c d e
print(piano_list[:5:2]) #a c e
print(piano_list[0:])   #a b c d e f g
print(piano_list[1:])   #b c d e f g
print(piano_list[:-1])  #a b c d e f
print(piano_list[:len(piano_list) - 1]) #a b c d e f
print(piano_list[:len(piano_list)]) #a b c d f g
print(piano_list[::])   #a b c d e f g
print(piano_list[::-1]) #g f e d c b a
print(piano_list[::-2]) #g e c a

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print()
print(piano_tuple[:4])  # do re mi fa
