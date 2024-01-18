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

food_list = ["Chicken", "Lamb", "Salmon", "Kebabs", "Pizza", "Burger"]
drink_list = ["Lemonade", "Soda", "Juice", "White Wine", "Red Wine", "Beer"]
dessert_list = ["Ice Cream", "Fruit", "Brownies", "Pudding", "Cheesecake", "Cookie"]

# create food items
food_variables = []
food_box = []
food_text = []
for counter, food in enumerate(food_list):
    food_var = IntVar()
    food_variables.append(food_var)

    # checkbox
    check_button = Checkbutton(
        food_panel,
        text=food.title(),
        font=("Doris", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=food_var,
    )
    check_button.grid(row=counter, column=0, sticky=W)

    # create input boxes
    text_var = StringVar()
    text_var.set("0")
    food_text.append(text_var)
    food_entry = Entry(
        food_panel,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=text_var,
    )

    food_box.append(food_entry)
    food_entry.grid(row=counter, column=1)

# create drink items
drink_variables = []
drink_box = []
drink_text = []
for counter, drink in enumerate(drink_list):
    drink_var = IntVar()
    drink_variables.append(drink_var)

    # checkbox
    check_button = Checkbutton(
        drink_panel,
        text=drink.title(),
        font=("Doris", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=drink_var,
    )
    check_button.grid(row=counter, column=0, sticky=W)

    # create input boxes
    text_var = StringVar()
    text_var.set("0")
    drink_text.append(text_var)
    drink_entry = Entry(
        drink_panel,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=text_var,
    )

    drink_box.append(drink_entry)
    drink_entry.grid(row=counter, column=1)

# create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
for counter, dessert in enumerate(dessert_list):
    dessert_var = IntVar()
    dessert_variables.append(dessert_var)

    # checkbox
    check_button = Checkbutton(
        dessert_panel,
        text=dessert.title(),
        font=("Doris", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=dessert_var,
    )
    check_button.grid(row=counter, column=0, sticky=W)

    # create input boxes
    text_var = StringVar()
    text_var.set("0")
    dessert_text.append(text_var)
    dessert_entry = Entry(
        dessert_panel,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=text_var,
    )

    dessert_box.append(dessert_entry)
    dessert_entry.grid(row=counter, column=1)


food_cost_var = StringVar()

# cost labels and input fields
food_cost_label = Label(
    cost_panel, text="Food Cost", font=("Doris", 12, "bold"), bg="azure4", fg="white"
)

food_cost_label.grid(row=0, column=0)
food_cost_text = Entry(
    cost_panel,
    font=("Doris", 12, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=food_cost_var,
)
food_cost_text.grid(row=0, column=1)
# prevent window from closing
application.mainloop()
