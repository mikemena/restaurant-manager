from tkinter import LabelFrame, LEFT, FLAT


def create_panel_label(left_panel, panel_types, font_style, font_size):
    for panel_type in panel_types:
        panel = LabelFrame(
            left_panel,
            text=panel_type.title(),
            font=(font_style, font_size, "bold"),
            bd=0,
            relief=FLAT,
            fg="aquamarine4",
        )
        panel.pack(side=LEFT)
