from tkinter import *

# Initialize Tkinter
application = Tk()

# Window size
application.geometry("1020x630+0+0")

# prevent from maximiaing
application.resizable(False, False)

# window title
application.title("My Restaurant - Invoicing System")

# window background color
# https://www.plus2net.com/python/tkinter-colors.php
application.config(bg="antiquewhite4")

# top panel
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# title tag
title_tag = Label(
    top_panel,
    text="Invoicing System",
    fg="azure4",
    font=("Dosis", 58),
    bg="burlywood",
    width=27,
)

# prevent window from closing
application.mainloop()
