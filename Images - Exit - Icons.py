from tkinter import *
from PIL import ImageTk, Image  # It is used to import images easily

root = Tk()
root.title("Images - Exit - Icons")
# The icon
photo = PhotoImage(file="download.png")
root.iconphoto(False, photo)

# Using images
my_img = ImageTk.PhotoImage(Image.open("blahblah.png"))  # The PhotoImage is the same as before
my_label = Label(image=my_img)
# An exit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
