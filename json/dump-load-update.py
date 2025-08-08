import json 
web_json = {
    'Amazon' : {
        'email' : 'abc@email.com',
        'password' : "12133asadsm*"
    },
    'Google' : {
        'email' : 'abc@email.com',
        'password' : '212dads#vs'
    }
}


web_json_file = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/json/web-file.json"

#(A) WRITE the json object to json file.

with open(web_json_file, "w") as dump_file :
    json.dump(web_json, dump_file, indent=4)

#(B) READ the json object from json file    
with open(web_json_file, "r") as load_file :
    loaded_json = json.load(load_file)    
    print(loaded_json)

#(C) Update the json obj, Not the file
    new_json = {
        'ebay' : {
            'email' : 'abc@email.com',
            'password' : 'ew323c*12s'
        }
    }
    loaded_json.update(new_json)
    print(loaded_json)

#(D) Write to json file updated  json obj .   
    with open(web_json_file, "w") as dump_file :
        json.dump(loaded_json, dump_file, indent=4)

 