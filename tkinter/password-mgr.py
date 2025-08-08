import tkinter
from tkinter import END
#from tkinter import *
from tkinter import messagebox
import random

#------------------------------------------------
#Window
window =tkinter.Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20, bg="beige")

#------------------------------------------------
#Canvas
canvas = tkinter.Canvas()
canvas.config(width=200, height=200, bg="beige", highlightthickness=0)
img= tkinter.PhotoImage(file="/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/tkinter/logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0, column=1)

#------------------------------------------------
#Labels
website_label = tkinter.Label(text="               WEBSITE : ")
website_label.config(pady=8, fg="blue", bg="beige" )
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="EMAIL/UserName : ")
email_label.config(pady=8, fg="blue", bg="beige")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="             PASSWORD : ")
password_label.config(pady=8, fg="blue", bg="beige")
password_label.grid(row=3, column=0)

#------------------------------------------------
#Entry
website_entry = tkinter.Entry(width=80)
website_entry.grid(row=1, column=1,columnspan=2)

email_entry = tkinter.Entry(width=80)
email_entry.insert(0, "abcd@email.com")
email_entry.grid(row=2, column=1,columnspan=2)

password_entry = tkinter.Entry(width=60)
password_entry.grid(row=3, column=1)

#------------------------------------------------
#Button command Functions

#(A) function write_to_file 
#command function for the Add Button
store_file="/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/tkinter/web-pass-STORE.txt"

def write_to_file() : 
  
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    line_list = [website_value, email_value, password_value]
    line_value = "|".join(line_list)
    
    #empty entries 
    if website_value == "" or password_value == "" :
        messagebox.showerror(title="Error", message="Empty Fields !")
    else :
    #write to file       
        with open(store_file, "a") as file :
    
            is_ok = messagebox.askokcancel(title="Confim", message=f"Do you Confirm to store into File\n Website :{website_value}\n Email : {email_value}\n Password :{password_value}")
        
            if is_ok :
                file.write(f"{line_value}\n")
                messagebox.showinfo(title="success", message="DONE !")

            website_entry.delete(0, END)    
            password_entry.delete(0, END)

#(B) function generate_passwd 
#command function for the Generate Password Button
def generate_password() :
    
    #password conditions: total digits=16 , minimum 8digit alphabets, minimum 2 special character, minimum 2 nunmbers
    #password(16 digit) = >8(alpha) + >2(nums) + >2(special_chars)

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    specials = ['@', '#', '$', '%', '&', '*', '-', '_', '+', ':', ';', '?', '<', '>']
    
    total_count=16
    alpha_count = random.randint(8, 12)
    num_count = random.randint(2, total_count - alpha_count - 2)
    specials_count = random.randint(2, total_count - alpha_count - num_count)

    alpha_list = [ random.choice(alphabets) for _ in range (0,alpha_count) ]
    num_list = [ random.choice(numbers) for _ in range(0,num_count) ]
    specials_list = [ random.choice(specials) for _ in range (0,specials_count) ]
    
    password_list =[]
    password_list += [_ for _ in alpha_list]
    password_list += [_ for _ in num_list]
    password_list += [_ for _ in specials_list]

    #print(f"password_list = {password_list}")
    
    random.shuffle(password_list)
    #print(f"password_list = {password_list}")

    password_str = "".join(password_list)

    print(f"password_str = {password_str}")
    #add password str to the entry
    password_entry.insert(0, password_str)

#------------------------------------------------
#Buttons
generate_btn = tkinter.Button(text="Generate Password", command=generate_password)
generate_btn.config(padx=5, fg="green", bg="silver")
generate_btn.grid(row=3, column=2)

add_btn = tkinter.Button(text="ADD", command=write_to_file)
add_btn.config(width=50 , fg="red", bg="silver")
add_btn.grid(row=4, column=1,)
add_btn.focus()
#------------------------------------------------


window.mainloop()
