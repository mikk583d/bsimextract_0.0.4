"""
Frame for displaying Start data visually
This will be showing the raw data in a table so the user can see the data has been imported correctly
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
import tkinter as tk

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from func.figures.random_plot import TestTable
from func.scrollableimage import ScrollableImage


class display_start(ctk.CTkFrame):
    def __init__(self, parent, new_data_var):
        super().__init__(master = parent)

        # layout
        self.rowconfigure((0), weight = 1)
        self.columnconfigure((0), weight = 1)

        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # label
        ctk.CTkLabel(self, text = "Welcome to BSimExtract!\n\nThis program is designed to extract and analyze data from .txt files from BSim.\nIt provides a user-friendly interface for visualizing and manipulating the extracted data.\nWith BSimExtract, you can easily import .txt files, convert them to dataframes, and generate insightful plots and tables.\nGet ready to explore and analyze your data with ease!", font = title_font).grid(row = 0, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)

        # table data
        
        
        new_data_var.trace("w", lambda name, index, mode, var=new_data_var: add_plot(self, var))

        def add_plot(self, new_data_var):
            imported_data = False
            if new_data_var.get() == True:
                imported_data = True
                print(imported_data)

            if imported_data == True:
                # Create a table plot with imported data
                plot = TestTable(self, size_y=70, size_x=30)
                img = tk.PhotoImage(file='figures output/TestTable.png')
                image_window = ScrollableImage(self, image = img, scrollbarwidth=20).grid(row=0, column=0, sticky="nsew")


        


if __name__ == "__main__":
    root = ctk.CTk()

    ctk.set_appearance_mode(COLOR_MODE)

    root.title("TEST: display_start")
    root.geometry("800x300")

    display_start(root).pack()

    root.mainloop()