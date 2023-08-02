from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()


# Put the function in the command
# The text will be displayed on the button
# The (fg) is color of the text - (bg) color of the background of the button

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")  # if I want to change how wide it is I just add (padx=50)
myButton.pack()

root.mainloop()
