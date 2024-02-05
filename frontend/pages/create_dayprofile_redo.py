"""
Toplevel page for creating a custom dayprofile
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk
import CTkMessagebox as CTkMessagebox
from CTkMenuBar import *
import webbrowser

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES

from settings.settings import *
from frontend.widgets.create_dayprofile_widgets.create_dayprofile_checkbox import *

class create_dayprofile(ctk.CTkToplevel):
    def __init__(self, parent, text_top_title = "Create a new dayprofile:"):
        super().__init__(master = parent)

        # setup
        self.title(text_top_title)
        self.geometry("700x875")
        #* Looking the size of the top level window because of performance hit when resizing
        self.minsize(700, 875)
        self.maxsize(700, 875)

        # grid layout
        self.columnconfigure((1, 2, 4), weight = 1)
        self.columnconfigure((0, 3), weight = 2)
        self.columnconfigure((5), weight = 3)
        # self.rowconfigure((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), weight=1)
        # self.columnconfigure((1), weight = 3)
        # total_width = 1000
        
        # font
        title_font = ctk.CTkFont(family=TITLE_FONT, size=TITLE_SIZE, weight=TITLE_WEIGHT)
        text_font = ctk.CTkFont(family=TEXT_FONT, size=TEXT_SIZE, weight=TEXT_WEIGHT)

        # text
        ctk.CTkLabel(self, text = "Please mark all the boxes that the dayprofile should be active for", font = title_font).grid(row = 0, column = 0, columnspan = 5, sticky = "nsew", padx = 5, pady = 5)
        # ctk.CTkLabel(self, text = "!This will be changed to a 'select name widget'!", font = text_font).grid(row = 0, column = 5, columnspan = 1, rowspan = 2, sticky = "nsew", padx = 5, pady = 5)
        ctk.CTkLabel(self, text = "Hours:", font = text_font).grid(row = 1, rowspan = 1, column = 4, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Days:", font = text_font).grid(row = 1, rowspan = 1, column = 3, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Weeks:", font = text_font).grid(row = 1, columnspan = 2, column = 1, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Months:", font = text_font).grid(row = 1, rowspan = 1, column = 0, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)
        ctk.CTkLabel(self, text = "Please write suffixation here:", font = text_font).grid(row = 0, column = 5, sticky = "nsew", padx = STANDARD_PADX, pady = STANDARD_PADY)


        # button
        ctk.CTkButton(self, text = "Save", command = lambda: self.save(name_var.get()), font = text_font).grid(row = 2, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        ctk.CTkButton(self, text = "Open", command = self.open, font = text_font).grid(row = 3, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "Exit", command = lambda: create_dayprofile.destroy(self), font = text_font).grid(row = 4, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        ctk.CTkButton(self, text = "All hours", command = self.all_hours, font = text_font).grid(row = 6, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "All days", command = self.all_days, font = text_font).grid(row = 7, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "All weeks", command = self.all_weeks, font = text_font).grid(row = 8, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        ctk.CTkButton(self, text = "All months", command = self.all_months, font = text_font).grid(row = 9, rowspan = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        # textbox
        #! Add an entry widget which name gets saved as a variable used as suffixation when saving the dayprofile
        name_var = ctk.StringVar(self)
        ctk.CTkEntry(self, textvariable = name_var, font = text_font).grid(row = 1, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        
        #* TESTES may be deleted later!
        # ctk.CTkButton(self, text = "test", command = lambda: print(name_var.get()), font = text_font).grid(row = 10, column = 5, sticky = "ew", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)
        # all_var_months = ctk.BooleanVar(root)
        # ctk.CTkButton(self, text = "All months", variable = all_var_months, command = lambda: toggle_all(month_var, all_var_months), font = text_font).grid(row = 8, rowspan = 1, column = 5, sticky = "ew", padx = 5, pady = 5)
        #* TESTES may be deleted later!

        # checkboxes
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_var = [ctk.BooleanVar(self) for _ in range(len(months))]
        month_checkboxes = [ctk.CTkCheckBox(self, text=month, variable=month_var[i]) for i, month in enumerate(months)]
        for i, month_checkboxes in enumerate(month_checkboxes):
            month_checkboxes.grid(row=i+2, column=0, sticky="s", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        weeks_first_half = [str(i) for i in range(0, 27)]
        week_var_first_half = [ctk.BooleanVar(self) for _ in range(len(weeks_first_half))]
        weeks_checkboxes_first_half = [ctk.CTkCheckBox(self, text=week, variable=week_var_first_half[i]) for i, week in enumerate(weeks_first_half)]
        for i, week_checkboxes in enumerate(weeks_checkboxes_first_half):
            week_checkboxes.grid(row=i+2, column=1, sticky="s", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        weeks_second_half = [str(i) for i in range(27, 53)]
        week_var_second_half = [ctk.BooleanVar(self) for _ in range(len(weeks_second_half))]
        weeks_checkboxes_second_half = [ctk.CTkCheckBox(self, text=week, variable=week_var_second_half[i]) for i, week in enumerate(weeks_second_half)]
        for i, week_checkboxes in enumerate(weeks_checkboxes_second_half):
            week_checkboxes.grid(row=i+2, column=2, sticky="s", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_var = [ctk.BooleanVar(self) for _ in range(len(days))]
        day_checkboxes = [ctk.CTkCheckBox(self, text=day, variable=day_var[i]) for i, day in enumerate(days)]
        for i, day_checkboxes in enumerate(day_checkboxes):
            day_checkboxes.grid(row=i+2, column=3, sticky="s", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        hours = [str(i) for i in range(0, 24)]
        hour_var = [ctk.BooleanVar(self) for _ in range(len(hours))]
        hour_checkboxes = [ctk.CTkCheckBox(self, text=hour, variable=hour_var[i]) for i, hour in enumerate(hours)]
        for i, hour_checkboxes in enumerate(hour_checkboxes):
            hour_checkboxes.grid(row=i+2, column=4, sticky="s", padx = STANDARD_PADX_CHECKBOX, pady = STANDARD_PADY_CHECKBOX)

        # def toggle_all(variables, current_var):
        #     toggle_value = current_var.get()
        #     for var in variables:
        #         var.set(toggle_value)
    

    def open(self):
            CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Opening of an existing dayprofile_XXX.txt file is not yet implemented", icon = "warning")
    
    def save(self, name_text = None):
        if len(name_text) == 0:
            CTkMessagebox.CTkMessagebox(title = "Error!", message = "You need to give you have a suffixation for your dayprofile to be able to save!", icon = "cancel")
        else:
            # Getting the values from the checkboxes
            CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Saving of the current file is not yet implemented", icon = "warning")


    def all_hours(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Toggling all hours is not yet implemented", icon = "warning")
    
    def all_days(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Togging all days is not yet implemented", icon = "warning")

    def all_weeks(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Togging all weeks is not yet implemented", icon = "warning")

    def all_months(self):
        CTkMessagebox.CTkMessagebox(title = "Not implemented yet", message = "Togging all months is not yet implemented", icon = "warning")




if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode(COLOR_MODE)
    root.geometry("200x50")
    create_dayprofile(root)
    root.mainloop()