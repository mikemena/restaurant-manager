from tkinter import LabelFrame, LEFT, FLAT


def create_panel(parent, title, font_style, font_size):
    panel = LabelFrame(
        parent,
        text=title,
        font=(font_style, font_size, "bold"),
        bd=0,
        relief=FLAT,
        fg="aquamarine4",
    )
    panel.pack(side=LEFT)
    return panel
