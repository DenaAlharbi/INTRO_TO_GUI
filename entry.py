from tkinter import *

root = Tk()

# This creates an input box with a text and specific size
# The (fg) is color of the text - (bg) color of the background of the button
# There is something called (borderwidth) that you could add to the first line

e = Entry(root, width=20, font=('Helvetica', 24))  # This alone creates an input box
e.pack()

# Put a default text inside the box
# e.insert(0, "Enter Your Name: ") //There is something wrong with this


def myClick():
    hello = "Hello " + e.get() + "!"
    myLabel = Label(root, text=hello)  # This enters the text based on the variable
    # e.delete(0, 'end')
    myLabel.pack()


# Put the function in the command
# The text will be displayed on the button
# The (fg) is color of the text - (bg) color of the background of the button

myButton = Button(root, text="Click Me!", command=myClick)  # if I want to change how wide it is I just add (padx=50)
myButton.pack()

root.mainloop()
