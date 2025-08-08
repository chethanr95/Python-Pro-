import tkinter

#Window
my_window = tkinter.Tk()
my_window.minsize(width=500, height=150)
my_window.title("miles_to_kms")
my_window.config(padx= 50, pady=15)

#Entry 
my_entry = tkinter.Entry(width=40)
my_entry.grid(row=0, column=1)

FONT=("arial", 12, "normal")
#label1
my_label1 = tkinter.Label(text="miles", font=FONT)
my_label1.grid(row=0, column=2)
my_label1.config(padx=20)

#label2
my_label2 = tkinter.Label(text="is equal to ", font=FONT)
my_label2.grid(row=1, column=0)

#label3 
my_label3 = tkinter.Label(text=0, font=FONT)
my_label3.grid(row=1, column=1)

#my_label4
my_label4 = tkinter.Label(text="KMs", font=FONT)
my_label4.grid(row=1, column=2)

#Button
#trigger method
def on_click() :
    miles = my_entry.get()
    miles = int(miles)
    kms = miles * 1.60
    my_label3.config(text=kms)

my_button = tkinter.Button(text="Calculte", command=on_click)
my_button.grid(row=2,column=1)











my_window.mainloop()