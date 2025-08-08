template_file = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/mail-merger/Input/Letters/starting_letter.txt"
invitees_file = "./Input/Names/invited_names.txt"

#(A)create list with names of invitees

#with open(invitees_file, mode="r") as invitees_fh :
#with open("./Input/Names/invited_names.txt", mode="r") as invitees_fh :    
with open("/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/mail-merger/Input/Names/invited_names.txt", mode="r") as invitees_fh :    

    invitees_list = invitees_fh.readlines()

#(B)create list with lines of the template file
with open(template_file) as letter_fh :
    template_file_list = letter_fh.readlines()
    #print(template_file_list)


#\n to be removed beside each name 
for i in range(0, len(invitees_list)) :
    name = invitees_list[i]
    name.strip()
    invitees_list[i] = name
    #print(name)
    name.replace('\n','')
    name.strip()
    #print(name)
    i +=1

#(B) Create output file

for name in invitees_list :
    output_folder = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/mail-merger/ReadyToSend"
    output_file = output_folder + "/letter_to_" + name + ".txt"
    #print(f"=={output_file}==")

    first_line = template_file_list[0]
    first_line.replace("[name]", name.strip())
    print(f"first_line = {first_line}")

    for line in template_file_list :
        with open(output_file, mode="w") as out_fh :
            out_fh.write(line)


