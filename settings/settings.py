"""
Settings for bsimextract
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import customtkinter as ctk

"""
Importing internal modules
"""
# #* IMPORTANT: DO NOT CHANGE THESE LINES
# import os
# import sys
# sys.path = os.getcwd()
# #* IMPORTANT: DO NOT CHANGE THESE LINES


#! Colors
# Source: https://www.color-hex.com/color-palette/78917
#* Main program colors
COLOR_1 = "#f6f6f4"
COLOR_2 = "#edeae5"
COLOR_3 = "#ced9dd"
COLOR_4 = "#979fa5"
COLOR_5 = "#2f3d4c"
#* Widget fg color
FG_COLOR = "transparent"
#* Table formatting colors
COLORS = [
    ("Red", "#ff0000"),
    ("Lime", "#00ff00"),
    ("Blue", "#0000ff"),
    ("Purple", "#800080"),
    ("Orange", "#ffa500"),
    ("Yellow", "#ffff00"),
    ("Green", "#008000"),
    ("Teal", "#008080"),
    ("Aqua", "#00ffff"),
    ("Fuchsia", "#ff00ff")
]

#! Appearance
COLOR_MODE = "dark"
# COLOR_MODE = "light"

#! Grid structure
#* Standard column width
STANDARD_COLUMN_WIDTH_TOTAL = 300
STANDARD_COLUMN_WIDTH_2 = STANDARD_COLUMN_WIDTH_TOTAL / 2
STANDARD_COLUMN_WIDTH_2_3 = (STANDARD_COLUMN_WIDTH_TOTAL / 3) * 2
STANDARD_COLUMN_WIDTH_3 = STANDARD_COLUMN_WIDTH_TOTAL / 3
STANDARD_COLUMN_WIDTH_3_4 = (STANDARD_COLUMN_WIDTH_TOTAL / 4) * 3
STANDARD_COLUMN_WIDTH_4 = STANDARD_COLUMN_WIDTH_TOTAL / 4
STANDARD_COLUMN_WIDTH_4_5 = (STANDARD_COLUMN_WIDTH_TOTAL / 5) * 4
STANDARD_COLUMN_WIDTH_5 = STANDARD_COLUMN_WIDTH_TOTAL / 5

#* Standard padx and pady
STANDARD_PADX = 5
STANDARD_PADY = 5
STANDARD_PADX_CHECKBOX = 2
STANDARD_PADY_CHECKBOX = 2


#! Version
VERSION_NUMBER = "0.0.1"

#! Text settings
#* Fonts
TITLE_FONT = "montserrat"
TEXT_FONT = "montserrat"
TITLE_MENU_FONT = "montserrat"
PAGE_MENU_FONT = "montserrat"
#* Size
TITLE_SIZE = 14
TEXT_SIZE = 12
TITLE_MENU_SIZE = 12
PAGE_MENU_SIZE = 14
#* Weight
TITLE_WEIGHT = "bold"
TEXT_WEIGHT = "bold"
TITLE_MENU_WEIGHT = "normal"
PAGE_MENU_WEIGHT = "bold"

#! Start path
START_PATH = ""

#! Start dayprofile
DAYPROFILE_CO2 = ""
DAYPROFILE_TEMP = ""
DAYPROFILE_RH = ""
DAYPROFILE_AIRCH = "" 

#! Start CO2 settings
CO2_MAXCO2_ONE = 1000
CO2_MAXCO2_TWO = 1250
CO2_MAXCO2_THREE = 1500
CO2_FORMATCOLOR_ONE = "Yellow"
CO2_FORMATCOLOR_TWO = "Orange"
CO2_FORMATCOLOR_THREE = "Red"

#! Start Temp settings
TEMP_HOUR_100 = 100
TEMP_HOUR_25 = 25

TEMP_MINTEMP = 20
TEMP_MAXTEMP_100H = 27
TEMP_MAXTEMP_25H = 28
TEMP_FORMATCOLOR_MINTEMP = "Aqua"
TEMP_FORMATCOLOR_MAXTEMP_100H = "Orange"
TEMP_FORMATCOLOR_MAXTEMP_25H = "Red"

TEMP_BETWEEN_MAX_SUMMER = 26
TEMP_BETWEEN_MIN_SUMMER = 22
TEMP_BETWEEN_MAX_TRANS = 26
TEMP_BETWEEN_MIN_TRANS = 21
TEMP_BETWEEN_MAX_WINTER = 25
TEMP_BETWEEN_MIN_WINTER = 21
TEMP_FORMATCOLOR_BETWEEN = "Purple"

#! Start RH settings
RH_MINRH = 30
RH_LOWMAXRH = 45
RH_MAXRH = 70
RH_FORMATCOLOR_MINRH = "Aqua"
RH_FORMATCOLOR_LOWMAXRH = "Orange"
RH_FORMATCOLOR_MAXRH = "Red"

#! Start Airch settings
AIRCH_MAXAIRCH_ONE = 2
AIRCH_MAXAIRCH_TWO = 3
AIRCH_MAXAIRCH_THREE = 4
AIRCH_FORMATCOLOR_ONE = "Yellow"
AIRCH_FORMATCOLOR_TWO = "Orange"
AIRCH_FORMATCOLOR_THREE = "Red"

