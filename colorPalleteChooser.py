# Import the library
from tkinter import *
from tkinter import colorchooser

# Create an instance of window
win=Tk()

# Set the geometry of the window
win.geometry("700x350")

# Create a label widget
label=Label(win, text="This is a new Label text", font=('Arial 17 bold'))
label.place(relx=0.5, rely=0.2, anchor = CENTER)

# Call the function to display the color palette
color=colorchooser.askcolor()

# Initialize the color range by picking up the first color
colorname=color[1]

# Configure the background color
win.configure(background=colorname)

win.mainloop()