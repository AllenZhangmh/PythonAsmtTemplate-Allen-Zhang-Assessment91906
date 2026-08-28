# Second-Hand Marketplace V4 GUI

import tkinter as tk
from tkinter import messagebox

# Platform charges a 5% fee when an item is sold
FEE_RATE = 0.05

# Store all items for sale
marketplace = []

# MAIN PAGE
def main_page():

    clear_page()

    tk.Label(
        window,
        text="Second-Hand Marketplace",
        font=("Arial", 22)
    ).pack(pady=30)

    tk.Button(
        window,
        text="Sell an Item",
        width=25,
        command=sell_page
    ).pack(pady=10)

    tk.Button(
        window,
        text="Buy / Search / View",
        width=25,
        command=market_page
    ).pack(pady=10)

    tk.Button(
        window,
        text="Quit",
        width=25,
        command=window.destroy
    ).pack(pady=10)

# SELL PAGE
def sell_page():

    clear_page()

    tk.Label(
        window,
        text="Sell an Item",
        font=("Arial", 20)
    ).pack(pady=15)

    tk.Label(window, text="Item Name").pack()

    item_entry = tk.Entry(window)
    item_entry.pack()

    tk.Label(window, text="Original Price ($)").pack()

    price_entry = tk.Entry(window)
    price_entry.pack()

    tk.Label(
        window,
        text="Condition (new/good/fair/poor)"
    ).pack()

    condition_entry = tk.Entry(window)
    condition_entry.pack()

    tk.Label(
        window,
        text="Your Own Selling Price ($)"
    ).pack()

    custom_price_entry = tk.Entry(window)
    custom_price_entry.pack()

    # Sell function
    def sell():

        item = item_entry.get()

        try:
            price = float(price_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter a valid price."
            )
            return

        condition = condition_entry.get().lower()

        # Calculate recommended price
        if condition == "new":
            recommended_price = price * 0.8

        elif condition == "good":
            recommended_price = price * 0.6

        elif condition == "fair":
            recommended_price = price * 0.4

        elif condition == "poor":
            recommended_price = price * 0.2

        else:
            messagebox.showerror(
                "Error",
                "Invalid condition."
            )
            return

        # Ask seller about recommended price
        accept = messagebox.askyesno(
            "Recommended Price",
            "Recommended Selling Price: $"
            + str(round(recommended_price, 2))
            + "\n\nDo you accept this price?"
        )

        if accept:

            sell_price = recommended_price

        else:

            try:
                sell_price = float(
                    custom_price_entry.get()
                )

                if sell_price <= 0:
                    messagebox.showerror(
                        "Error",
                        "Selling price must be greater than 0."
                    )
                    return

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Please enter a valid price."
                )
                return

        # Confirm listing
        confirm = messagebox.askyesno(
            "Confirm Listing",
            "Item: " + item
            + "\nFinal Selling Price: $"
            + str(round(sell_price, 2))
            + "\nCondition: " + condition
            + "\n\nList this item?"
        )

        if confirm:

            marketplace.append({
                "name": item,
                "price": sell_price,
                "condition": condition
            })

            messagebox.showinfo(
                "Success",
                "Item listed successfully!"
            )

            item_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            condition_entry.delete(0, tk.END)
            custom_price_entry.delete(0, tk.END)

    tk.Button(
        window,
        text="List Item",
        width=20,
        command=sell
    ).pack(pady=15)

    tk.Button(
        window,
        text="Back",
        width=20,
        command=main_page
    ).pack()

# BUY / SEARCH / VIEW PAGE
def market_page():

    clear_page()

    tk.Label(
        window,
        text="Buy / Search / View Items",
        font=("Arial", 20)
    ).pack(pady=15)

    # Search
    tk.Label(
        window,
        text="Search Item"
    ).pack()

    search_entry = tk.Entry(window)
    search_entry.pack()

    # Listbox
    listbox = tk.Listbox(
        window,
        width=55,
        height=10
    )

    listbox.pack(pady=10)

    # Display all items
    def view_items():

        listbox.delete(0, tk.END)

        if len(marketplace) == 0:

            listbox.insert(
                tk.END,
                "There are no items for sale."
            )

        else:

            for i, item in enumerate(marketplace):

                listbox.insert(
                    tk.END,
                    str(i + 1)
                    + ". "
                    + item["name"]
                    + " - $"
                    + str(round(item["price"], 2))
                    + " - "
                    + item["condition"]
                )

    # Search items
    def search_items():

        listbox.delete(0, tk.END)

        search = search_entry.get().lower()

        for i, item in enumerate(marketplace):

            if search in item["name"].lower():

                listbox.insert(
                    tk.END,
                    str(i + 1)
                    + ". "
                    + item["name"]
                    + " - $"
                    + str(round(item["price"], 2))
                    + " - "
                    + item["condition"]
                )

    # Buy item
    def buy_item():

        selected = listbox.curselection()

        if not selected:

            messagebox.showerror(
                "Error",
                "Please select an item."
            )
            return

        item_number = selected[0]

        # Get selected item
        selected_item = marketplace[item_number]

        price = selected_item["price"]

        # Calculate platform fee
        fee = price * FEE_RATE

        seller_receives = price - fee

        confirm = messagebox.askyesno(
            "Confirm Purchase",
            "Item: " + selected_item["name"]
            + "\nPrice: $" + str(round(price, 2))
            + "\nPlatform Fee (5%): $"
            + str(round(fee, 2))
            + "\nSeller receives: $"
            + str(round(seller_receives, 2))
            + "\n\nBuy this item?"
        )

        if confirm:

            marketplace.pop(item_number)

            messagebox.showinfo(
                "Purchase Successful",
                "Purchase successful!"
            )

            view_items()

    # Buttons
    tk.Button(
        window,
        text="Search",
        width=15,
        command=search_items
    ).pack(pady=5)

    tk.Button(
        window,
        text="View All Items",
        width=15,
        command=view_items
    ).pack(pady=5)

    tk.Button(
        window,
        text="Buy Selected Item",
        width=15,
        command=buy_item
    ).pack(pady=5)

    tk.Button(
        window,
        text="Back",
        width=15,
        command=main_page
    ).pack(pady=10)

    # Show items when page opens
    view_items()

# CLEAR PAGE
def clear_page():

    for widget in window.winfo_children():
        widget.destroy()

# WINDOW
window = tk.Tk()

window.title("Second-Hand Marketplace")

window.geometry("550x600")

main_page()

window.mainloop()
    else:
        print("Invalid choice. Please try again.")

print("\nGoodbye!")
