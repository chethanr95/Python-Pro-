#module = pickle
#pickling = process of serializatoin  = converting python data object into a byte stream and stored into file
#pickle.dump(obj_name, fh)
#unpickling = process of deserialize = converting file of byte stream into a python data obj back
#pickle.load(fh)

import pickle

my_dict = {
    'first_name' : 'John',
    'age' : 30,
    'place' : 'Bangalore'
} 

myfile = "pickled.txt"

with open(myfile, 'wb') as fh : 
    pickle.dump(my_dict, fh)

my_dict['last_name'] = 'Doe'

print(type(my_dict))
print(my_dict)

with open(myfile, 'wb') as fh :
    pickle.dump(my_dict, fh)

with open(myfile, 'rb') as fh :
    new_dict = pickle.load(fh)
    print(type(new_dict))
    print(new_dict)

