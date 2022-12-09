from tkinter import *
from cell import Cell
import settings, utils


calc_prct = utils.CalculatePercentage()

# Instantiate a "Tkinter" window instance
root = Tk()
# Start: Override the settings of the window
root.configure(bg='black')    # config the bg-color of the window
# Modify window form appearance
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')   # Size of the window: ('WIDTH*HEIGHT'); hard-coded value: WIDTH=1080; HEIGHT=720
root.title("Minesweeper")    # title of the window
root.resizable(False, False)    # make window size fized (WIDTH:bool, HEIGHT:bool)
# End: Override the settings of the window

# Code Start: Inside Tkinter
# Frame: Divide the window into sections
# Frame-1: Top Panel
top_frame = Frame(
    root,
    bg='black',   # change later to black
    width=settings.WIDTH, # cover entire window-width
    height=calc_prct.height_prct(25)  # 1/4 of the window-height (25%); hard-coded value: 180; calculate dynamically in utils.py file;

) # Instantiate 'Frame' class; locate later
top_frame.place(x=0, y=0)   # specify x-axis, y-axis
# Frame-2: Left Side Bar
left_frame = Frame(
    root,
    bg='black',
    width=calc_prct.width_prct(20),  # 1/5 of the window-width (20%) ; hard-coded value: 216; calculate dynamically in utils.py file;
    height=calc_prct.height_prct(75)  # substract 720-180; 75% of the total height; hard-coded value: 540
)
left_frame.place(x=0, y=calc_prct.height_prct(25))    # 25% of the entire window-height; hard-coded value: 180
# Frame-3: Game board layout; Center of the page
center_frame = Frame(
    root,
    bg='purple',
    width=calc_prct.width_prct(80),
    height=calc_prct.width_prct(75),
)
center_frame.place(x=calc_prct.width_prct(20), y=calc_prct.height_prct(25)) # according to width of "left_frame" & height of "top_frame"

# Place a button in the center_frame
# btn1 = Button(
#     center_frame,
#     bg='blue',
#     text='First Button'
# )
# btn1.place(x=0, y=0)

# Instantiate 'Cell' class; create btn-object
c1 = Cell()
c1.create_btn_object(location=center_frame)
# Instead of 'palce()' method, use 'grid()' method; while palcing multiple similar object in a certain frame dynamically
c1.cell_btn_obj.grid(
    column=0, row=0
)

c2 = Cell()
c2.create_btn_object(location=center_frame)
c2.cell_btn_obj.grid(
    column=0, row=1
)

# Code End: Inside Tkinter

# Run the Tkinter window instance
root.mainloop()
