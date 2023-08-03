from tkinter import *

root = Tk()
root.title("Images - Exit - Icons")
# The icon
photo = PhotoImage(file="download.png")
root.iconphoto(False, photo)

# An exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()