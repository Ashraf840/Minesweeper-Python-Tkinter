from tkinter import Button

# Abstract the button with a custom class; since there will be 36 cell-buttons in different positions, 
# mines & logics, overall some attributes to the button regarding the "Cells & Mines",
# thus create a cell call & create a custom method to instantiate the "Button" object.

class Cell:
    """
    This class contains the "cells & mines" logics. 
    Instantiate a button-class-object from Tkinter using method. 
    """
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
    
    def create_btn_object(self, location):
        """
        Create a button-obj & define the location of the btn using location-param. 
        Assign the variable with this instance attribute, consequently the instance-attribute 
        can be used for placing in certain frames.
        """
        btn = Button(
            location,
            text='Text'
        )
        self.cell_btn_obj = btn   # Used to place the btn-object using ".place()" method. Instead of 'place()' method, use 'grid()' when creating & placing a collectio of similar element dynamically.
