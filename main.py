from tkinter import *
import settings

# Instantiate a "Tkinter" window instance
root = Tk()
# Start: Override the settings of the window
root.configure(bg='black')    # config the bg-color of the window
# Modify window form appearance
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')   # Size of the window: ('WIDTH*HEIGHT')
root.title("Minesweeper")    # title of the window
root.resizable(False, False)    # make window size fized (WIDTH:bool, HEIGHT:bool)
# End: Override the settings of the window

# Code Start: Inside Tkinter
# Frame: Divide the window into sections
# Frame-1: Top Panel
top_frame = Frame(
    root,
    bg='red',   # change later to black
    width=1080, # cover entire window-width
    height=180  # 1/4 of the window-height

) # Instantiate 'Frame' class; locate later
top_frame.place(x=0, y=0)   # specify x-axis, y-axis
# Frame-2: Left Side Bar
left_frame = Frame(
    root,
    bg='gray',
    width=216,  # 1/5 of the window-width
    height=540  # substract 720-180
)
left_frame.place(x=0, y=180)


# Code End: Inside Tkinter

# Run the Tkinter window instance
root.mainloop()
