# Second-Hand Marketplace V2

import tkinter as tk
from tkinter import messagebox

FEE_RATE = 0.05
marketplace = []


# SELL
def sell_item():
    item = item_entry.get()
    
    try:
        price = float(price_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price.")
        return

    condition = condition_entry.get().lower()

    if condition == "new":
        sell_price = price * 0.8
    elif condition == "good":
        sell_price = price * 0.6
    elif condition == "fair":
        sell_price = price * 0.4
    elif condition == "poor":
        sell_price = price * 0.2
    else:
        messagebox.showerror("Error", "Invalid condition.")
        return

    marketplace.append({
        "name": item,
        "price": sell_price,
        "condition": condition
    })

    messagebox.showinfo(
        "Item Listed",
        "Item: " + item +
        "\nRecommended Price: $" + str(round(sell_price, 2))
    )

    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    condition_entry.delete(0, tk.END)


# VIEW
def view_items():
    items_text.delete("1.0", tk.END)

    if len(marketplace) == 0:
        items_text.insert(tk.END, "There are no items for sale.")
        return

    for i, item in enumerate(marketplace):
        items_text.insert(
            tk.END,
            str(i + 1) + ". " +
            item["name"] +
            " - $" + str(round(item["price"], 2)) +
            " - " + item["condition"] + "\n"
        )


# SEARCH
def search_items():
    search = search_entry.get().lower()
    items_text.delete("1.0", tk.END)

    found = False

    for i, item in enumerate(marketplace):
        if search in item["name"].lower():
            items_text.insert(
                tk.END,
                str(i + 1) + ". " +
                item["name"] +
                " - $" + str(round(item["price"], 2)) +
                " - " + item["condition"] + "\n"
            )
            found = True

    if not found:
        items_text.insert(tk.END, "No items found.")


# BUY
def buy_item():
    try:
        number = int(buy_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid item number.")
        return

    if number < 1 or number > len(marketplace):
        messagebox.showerror("Error", "Invalid item number.")
        return

    selected_item = marketplace[number - 1]

    price = selected_item["price"]
    fee = price * FEE_RATE
    seller_receives = price - fee

    messagebox.showinfo(
        "Purchase Successful",
        "Item: " + selected_item["name"] +
        "\nPrice: $" + str(round(price, 2)) +
        "\nPlatform Fee (5%): $" + str(round(fee, 2)) +
        "\nSeller receives: $" + str(round(seller_receives, 2))
    )

    marketplace.pop(number - 1)
    buy_entry.delete(0, tk.END)
    view_items()


# GUI
window = tk.Tk()
window.title("Second-Hand Marketplace")
window.geometry("600x650")

title = tk.Label(
    window,
    text="Second-Hand Marketplace",
    font=("Arial", 20)
)
title.pack(pady=10)


# SELL SECTION
sell_frame = tk.LabelFrame(window, text="Sell an Item")
sell_frame.pack(padx=20, pady=10, fill="x")

tk.Label(sell_frame, text="Item name:").grid(row=0, column=0)
item_entry = tk.Entry(sell_frame)
item_entry.grid(row=0, column=1)

tk.Label(sell_frame, text="Original price:").grid(row=1, column=0)
price_entry = tk.Entry(sell_frame)
price_entry.grid(row=1, column=1)

tk.Label(sell_frame, text="Condition:").grid(row=2, column=0)
condition_entry = tk.Entry(sell_frame)
condition_entry.grid(row=2, column=1)

tk.Button(
    sell_frame,
    text="Sell Item",
    command=sell_item
).grid(row=3, column=0, columnspan=2, pady=5)


# SEARCH SECTION
search_frame = tk.LabelFrame(window, text="Search Items")
search_frame.pack(padx=20, pady=10, fill="x")

search_entry = tk.Entry(search_frame)
search_entry.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_items
).pack(side="left")


# BUY SECTION
buy_frame = tk.LabelFrame(window, text="Buy an Item")
buy_frame.pack(padx=20, pady=10, fill="x")

tk.Label(buy_frame, text="Item number:").pack(side="left")

buy_entry = tk.Entry(buy_frame)
buy_entry.pack(side="left", padx=5)

tk.Button(
    buy_frame,
    text="Buy Item",
    command=buy_item
).pack(side="left")


# VIEW SECTION
view_frame = tk.LabelFrame(window, text="Available Items")
view_frame.pack(padx=20, pady=10, fill="both", expand=True)

items_text = tk.Text(view_frame, height=12)
items_text.pack(fill="both", expand=True)

tk.Button(
    window,
    text="View All Items",
    command=view_items
).pack(pady=10)


window.mainloop()
