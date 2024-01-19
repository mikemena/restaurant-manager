from tkinter import *
from menu_items import create_menu_items
from panel_labels import create_panel_label

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
    fg="aquamarine4",
    font=("Dosis", 58),
    bg="antiquewhite3",
    width=27,
)
title_tag.grid(row=0, column=0)

# left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT)
cost_panel.pack(side=BOTTOM)

# panel_types = ["drink", "food", "dessert"]
# create_panel_label(left_panel, panel_types,"Dosis", 18)

# food panel
food_panel = LabelFrame(
    left_panel,
    text="Food",
    font=("Dosis", 18, "bold"),
    bd=0,
    relief=FLAT,
    fg="aquamarine4",
)
food_panel.pack(side=LEFT)

# drink panel
drink_panel = LabelFrame(
    left_panel,
    text="Drink",
    font=("Dosis", 18, "bold"),
    bd=0,
    relief=FLAT,
    fg="aquamarine4",
)
drink_panel.pack(side=LEFT)

# dessert panel
dessert_panel = LabelFrame(
    left_panel,
    text="Dessert",
    font=("Dosis", 18, "bold"),
    bd=0,
    relief=FLAT,
    fg="aquamarine4",
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

food_list = ["Chicken", "Lamb", "Salmon", "Kebabs", "Pizza", "Burger"]
drink_list = ["Lemonade", "Soda", "Juice", "White Wine", "Red Wine", "Beer"]
dessert_list = ["Ice Cream", "Fruit", "Brownies", "Pudding", "Cheesecake", "Cookie"]

# Example usage
food_variables, food_box, food_text = create_menu_items(
    food_panel, food_list, "Dosis", 18
)
drink_variables, drink_box, drink_text = create_menu_items(
    drink_panel, drink_list, "Dosis", 18
)
dessert_variables, dessert_box, dessert_text = create_menu_items(
    dessert_panel, dessert_list, "Dosis", 18
)


# variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()


# cost labels and input fields
food_cost_label = Label(
    cost_panel, text="Food Cost", font=("Doris", 18, "bold"), fg="aquamarine4"
)

food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(
    cost_panel,
    font=("Doris", 18, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=food_cost_var,
)
food_cost_text.grid(row=0, column=1, padx=40)

# drink labels and input fields
drink_cost_label = Label(
    cost_panel, text="Drink Cost", font=("Doris", 18, "bold"), fg="aquamarine4"
)

drink_cost_label.grid(row=1, column=0)
drink_cost_text = Entry(
    cost_panel,
    font=("Doris", 18, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=drink_cost_var,
)
drink_cost_text.grid(row=1, column=1)

# dessert labels and input fields
dessert_cost_label = Label(
    cost_panel,
    text="Dessert Cost",
    font=("Doris", 18, "bold"),
    fg="aquamarine4",
)

dessert_cost_label.grid(row=2, column=0)
dessert_cost_text = Entry(
    cost_panel,
    font=("Doris", 18, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=dessert_cost_var,
)
dessert_cost_text.grid(row=2, column=1)

# subtotal labels and input fields
subtotal_label = Label(
    cost_panel,
    text="Subtotal",
    font=("Doris", 18, "bold"),
    fg="aquamarine4",
)

subtotal_label.grid(row=0, column=2)
subtotal_text = Entry(
    cost_panel,
    font=("Doris", 18, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=subtotal_var,
)
subtotal_text.grid(row=0, column=3)

# taxes labels and input fields
taxes_label = Label(
    cost_panel,
    text="Taxes",
    font=("Doris", 18, "bold"),
    fg="aquamarine4",
)

taxes_label.grid(row=1, column=2)
taxes_text = Entry(
    cost_panel,
    font=("Doris", 12, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=taxes_var,
)
taxes_text.grid(row=1, column=3)

# total labels and input fields
total_label = Label(
    cost_panel,
    text="Total",
    font=("Doris", 18, "bold"),
    fg="aquamarine4",
)

total_label.grid(row=2, column=2)
total_text = Entry(
    cost_panel,
    font=("Doris", 12, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=total_var,
)
total_text.grid(row=2, column=3)

# prevent window from closing
application.mainloop()
