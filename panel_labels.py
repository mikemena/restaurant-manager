from tkinter import LabelFrame, LEFT, FLAT


def create_panel_label(panel_types, font_style, font_size):
    for panel_type in panel_types:
        panel = LabelFrame(
            left_panel,
            text="Drink",
            font=("Dosis", 18, "bold"),
            bd=0,
            relief=FLAT,
            fg="aquamarine4",
        )
        panel.pack(side=LEFT)
    return
