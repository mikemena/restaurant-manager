from tkinter import *

def create_menu_items(panel, item_list, font_style, font_size):
item_variables = []
item_boxes = []
item_text_vars = []

for counter, item in enumerate(item_list):
    item_var = StringVar()
