from typing import List, Tuple
from tkinter import (
    IntVar,
    Checkbutton,
    StringVar,
    Entry,
    W,
    DISABLED,
    NORMAL,
    END,
    Frame,
)


class MenuApp:
    def __init__(self, root, item_list, font_style, font_size):
        self.root = root
        self.item_list = item_list
        self.font_style = font_style
        self.font_size = font_size

        self.item_vars = []  # Store IntVar for checkboxes
        self.item_boxes = []  # Store Entry widgets
        self.item_text_vars = []  # Store StringVar for Entry widgets

        self.create_menu_items()

    # instance method
    def review_check(self):
        for i, item_box in enumerate(self.item_boxes):
            if self.item_vars[i].get() == 1:
                item_box.config(state=NORMAL)
                if item_box[1].get() == "0":
                    item_box.delete(0, END)
                item_box.focus()
            else:
                item_box.config(state=DISABLED)
                self.item_text_vars[i].set("0")

    def create_menu_items(self) -> Tuple[List[IntVar], List[Entry], List[StringVar]]:
        panel = Frame(self.root)
        panel.pack()

        for i, item in enumerate(self.item_list):
            item_var = IntVar()
            self.item_vars.append(item_var)

            # Create checkbox
            check_button = Checkbutton(
                panel,
                text=item.title(),
                font=(self.font_style, self.font_size, "bold"),
                onvalue=1,
                offvalue=0,
                variable=item_var,
                command=self.review_check,
            )
            check_button.grid(row=i, column=0, sticky=W)

            # Create input boxes
            text_var = StringVar(value="0")
            self.item_text_vars.append(text_var)
            item_entry = Entry(
                panel,
                font=(self.font_style, self.font_size, "bold"),
                width=6,
                state=DISABLED,
                textvariable=text_var,
            )
            self.item_boxes.append(item_entry)
            item_entry.grid(row=i, column=1)

        return self.item_vars, self.item_boxes, self.item_text_vars
