from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is dena!")
# Shoving it onto the screen
# myLabel.pack()  # make it according to the size of the text

# To make the size specific
myLabel.grid(row=0, column=0)   # The column is right and left / they are relative to each other
myLabel2.grid(row=1, column=0)  # This is in the bottom

root.mainloop()
