import tkinter

#window object
#from Tk() class of the tkinter library
window = tkinter.Tk()   #use along with obj.mainlook() method at the eof

window.title("First tkinter usage")
window.minsize(width=700, height=500)

MY_FONT=("Arial", 15, "normal")
#label
#syntax obj = tkinter.Label(text="" , font = (,,))
my_label = tkinter.Label(text="I am the Label", font = MY_FONT) #use along with obj.pack() method to show up in screen
my_label.pack()
#my_label.pack(side="left")


window.mainloop()