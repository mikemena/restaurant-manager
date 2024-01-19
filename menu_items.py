from tkinter import *


def create_menu_items(panel, item_list, font_style, font_size):
    item_variables = []
    item_boxes = []
    item_text_vars = []

    for counter, item in enumerate(item_list):
        item_var = IntVar()
        item_variables.append(item_var)

        # checkbox
        check_button = Checkbutton(
            panel,
            text=item.title(),
            font=(font_style, font_size, "bold"),
            onvalue=1,
            offvalue=0,
            variable=item_var,
        )
        check_button.grid(row=counter, column=0, sticky=W)

        # create input boxes
        text_var = StringVar()
        text_var.set("0")
        item_text_vars.append(text_var)
        item_entry = Entry(
            panel,
            font=(font_style, font_size, "bold"),
            width=6,
            state=DISABLED,
            textvariable=text_var,
        )

        item_boxes.append(item_entry)
        item_entry.grid(row=counter, column=1)

    return item_variables, item_boxes, item_text_vars
