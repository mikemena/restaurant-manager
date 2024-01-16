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
top_panel = Frame(application, bd=0, relief=FLAT)
top_panel.pack(side=TOP)

# title tag
title_tag = Label(
    top_panel,
    text="Invoicing System",
    fg="azure4",
    font=("Dosis", 58),
    bg="antiquewhite3",
    width=27,
)
title_tag.grid(row=0, column=0)

# left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# cost panel
cost_panel = Frame(application, bd=1, relief=FLAT)
cost_panel.pack(side=BOTTOM)

# food panel
food_panel = LabelFrame(
    left_panel, text="Food", font=("Dosis", 19, "bold"), bd=0, relief=FLAT, fg="azure4"
)
food_panel.pack(side=LEFT)

# drink panel
drink_panel = LabelFrame(
    left_panel, text="Drink", font=("Dosis", 19, "bold"), bd=0, relief=FLAT, fg="azure4"
)
drink_panel.pack(side=LEFT)

# dessert panel
dessert_panel = LabelFrame(
    left_panel,
    text="Dessert",
    font=("Dosis", 19, "bold"),
    bd=0,
    relief=FLAT,
    fg="azure4",
)
dessert_panel.pack(side=LEFT)

# right panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calculator panel
calculator_panel = Frame(right_panel, bd=0, relief=FLAT, bg="azure4")
calculator_panel.pack()

# invoice panel
invoice_panel = Frame(right_panel, bd=0, relief=FLAT, bg="azure4")
invoice_panel.pack()

# buttons panel
buttons_panel = Frame(right_panel, bd=0, relief=FLAT, bg="azure4")
buttons_panel.pack()

# prevent window from closing
application.mainloop()
