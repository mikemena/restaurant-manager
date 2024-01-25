from tkinter import (
    Tk,
    StringVar,
    Label,
    Frame,
    Button,
    Text,
    Entry,
    TOP,
    LEFT,
    RIGHT,
    BOTTOM,
    FLAT,
    END,
)
from menu_items import MenuApp
from panel_labels import create_panel
import random
import datetime

operator = ""
food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14]

# calculator buttons


def click_button(character):
    global operator
    operator = operator + character
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)


def delete_all():
    global operator
    operator = ""
    calculator_display.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ""


def total_calculation():
    tax_rate = 0.075

    def calculate_subtotal(menu, prices):
        subtotal = 0

        for i, item_var in enumerate(menu.item_text_vars):
            try:
                quantity = int(item_var.get())
                subtotal += quantity * prices[i]
            except ValueError:
                pass  # Ignore if the quantity is not a number
        return subtotal

    food_subtotal = calculate_subtotal(food_menu, food_price)
    drink_subtotal = calculate_subtotal(drink_menu, drink_price)
    dessert_subtotal = calculate_subtotal(dessert_menu, dessert_price)

    subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    taxes = subtotal * tax_rate
    total = subtotal + taxes

    subtotal_var.set(f"{subtotal:.2f}")  # Update the total in the UI
    taxes_var.set(f"{taxes:.2f}")  # Update the taxes in the UI
    total_var.set(f"{total:.2f}")  # Update the total in the UI

    # Update the subtotals in the UI
    food_cost_var.set(f"{food_subtotal:.2f}")
    drink_cost_var.set(f"{drink_subtotal:.2f}")
    dessert_cost_var.set(f"{dessert_subtotal:.2f}")


def create_invoice(menu_app, prices):
    selected_items_info = []
    for i, item_var in enumerate(menu_app.item_vars):
        if item_var.get() == 1:
            item_name = menu_app.item_list[i]
            try:
                quantity = int(menu_app.item_text_vars[i].get())
                price = prices[i]
                total_price = quantity * price
                selected_items_info.append((item_name, quantity, price, total_price))
            except ValueError:
                pass  # ignore if the quantity is not a number or is empty
    return selected_items_info


def generate_invoice():
    invoice_text.delete(1.0, END)

    # Header for invoice
    invoice_number = f"N# - {random.randint(1000, 9999)}"
    my_date = datetime.datetime.now()
    invoice_date = f"{my_date.month}/{my_date.day}/{my_date.year} - {my_date.hour}:{my_date.minute}"
    invoice_text.insert(END, f"Information: {invoice_number}\t\t{invoice_date}\n")
    invoice_text.insert(END, f"*" * 45 + "\n")
    invoice_text.insert(END, f"Items\t\tQuantity\tUnit Price\tTotal Cost\n")
    invoice_text.insert(END, f"*" * 45 + "\n")

    # Adding items to the invoice
    def add_items_to_invoice(items_info):
        for item_name, quantity, price, total_price in items_info:
            invoice_text.insert(
                END, f"{item_name}\t\t{quantity}\t{price}\t{total_price}\n"
            )

    # Get selected items information
    food_selected_info = create_invoice(food_menu, food_price)
    drink_selected_info = create_invoice(drink_menu, drink_price)
    dessert_selected_info = create_invoice(dessert_menu, dessert_price)

    # Add items to invoice
    add_items_to_invoice(food_selected_info)
    add_items_to_invoice(drink_selected_info)
    add_items_to_invoice(dessert_selected_info)

    # Calculate and display total
    total_calculation()
    invoice_text.insert(END, f"\nSubtotal: {subtotal_var.get()}\n")
    invoice_text.insert(END, f"Taxes: {taxes_var.get()}\n")
    invoice_text.insert(END, f"Total: {total_var.get()}\n")


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

# create menu item panels
food_panel = create_panel(left_panel, "Food", "Dosis", 18)
drink_panel = create_panel(left_panel, "Drink", "Dosis", 18)
dessert_panel = create_panel(left_panel, "Dessert", "Dosis", 18)


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
food_menu = MenuApp(food_panel, food_list, "Dosis", 18)
drink_menu = MenuApp(drink_panel, drink_list, "Dosis", 18)
dessert_menu = MenuApp(dessert_panel, dessert_list, "Dosis", 18)

food_selected_info = create_invoice(food_menu, food_price)
drink_selected_info = create_invoice(drink_menu, drink_price)
dessert_selected_info = create_invoice(dessert_menu, dessert_price)

print(food_selected_info)


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
    font=("Doris", 18, "bold"),
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
    font=("Doris", 18, "bold"),
    bd=0,
    width=10,
    state="readonly",
    textvariable=total_var,
)
total_text.grid(row=2, column=3)

# buttons
buttons = ["total", "invoice", "save", "reset"]
created_buttons = []
column = 0
for button in buttons:
    button = Button(
        buttons_panel,
        text=button.title(),
        font=("Doris", 14, "bold"),
        width=6,
        bg="antiquewhite4",
    )

    created_buttons.append(button)

    button.grid(row=0, column=column)

    column += 1

created_buttons[0].config(command=total_calculation)
created_buttons[1].config(command=generate_invoice)


# invoice section
invoice_text = Text(
    invoice_panel, font=("Dosis", 12, "bold"), bd=1, width=42, height=10
)
invoice_text.grid(row=0, column=0)

# calculator
calculator_display = Entry(calculator_panel, font=("Dosis", 16, "bold"), width=32, bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)

calculator_buttons = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "x",
    "CE",
    "Delete",
    "0",
    "/",
]

stored_buttons = []

my_row = 1
my_column = 0

for button in calculator_buttons:
    button = Button(
        calculator_panel,
        text=button.title(),
        font=("Dosis", 16, "bold"),
        fg="bisque4",
        bg="antiquewhite3",
        bd=1,
        width=5,
    )
    stored_buttons.append(button)

    button.grid(row=my_row, column=my_column)

    if my_column == 3:
        my_row += 1

    my_column += 1

    if my_column == 4:
        my_column = 0

stored_buttons[0].config(command=lambda: click_button("7"))
stored_buttons[1].config(command=lambda: click_button("8"))
stored_buttons[2].config(command=lambda: click_button("9"))
stored_buttons[3].config(command=lambda: click_button("+"))
stored_buttons[4].config(command=lambda: click_button("4"))
stored_buttons[5].config(command=lambda: click_button("5"))
stored_buttons[6].config(command=lambda: click_button("6"))
stored_buttons[7].config(command=lambda: click_button("-"))
stored_buttons[8].config(command=lambda: click_button("1"))
stored_buttons[9].config(command=lambda: click_button("2"))
stored_buttons[10].config(command=lambda: click_button("3"))
stored_buttons[11].config(command=lambda: click_button("*"))
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda: click_button("0"))
stored_buttons[15].config(command=lambda: click_button("/"))


# prevent window from closing
application.mainloop()
