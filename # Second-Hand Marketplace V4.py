# Second-Hand Marketplace V4
# This program allows users to sell, buy and search for second-hand items.
# Sellers can accept the recommended price or enter their own price.

print("Welcome to the Second-Hand Marketplace")

# Platform charges a 5% fee when an item is sold
FEE_RATE = 0.05

# Store all items for sale
marketplace = []

# Keep showing the menu until the user chooses to quit
while True:

    # Display the main menu
    print("\n--- Main Menu ---")
    print("1. Sell an item")
    print("2. Buy an item")
    print("3. Search items")
    print("4. View items")
    print("5. Quit")

    choice = input("Choose an option: ")

    # =========================
    # SELL AN ITEM
    # =========================
    if choice == "1":

        # Get information about the item
        item = input("\nEnter item name: ")
        price = float(input("Enter original price ($): "))
        condition = input(
            "Enter condition (new/good/fair/poor): "
        ).lower()

        # Calculate a recommended selling price
        # based on the condition of the item
        if condition == "new":
            recommended_price = price * 0.8

        elif condition == "good":
            recommended_price = price * 0.6

        elif condition == "fair":
            recommended_price = price * 0.4

        elif condition == "poor":
            recommended_price = price * 0.2

        else:
            # Stop if the condition is invalid
            print("Invalid condition. Please try again.")
            continue

        # Show the recommended price to the seller
        print("\nItem:", item)
        print("Original Price: $", round(price, 2))
        print(
            "Recommended Selling Price: $",
            round(recommended_price, 2)
        )

        # Ask the seller if they accept the recommended price
        accept = input(
            "Do you accept the recommended price? (yes/no): "
        ).lower()

        if accept == "yes":

            # Use the recommended price
            sell_price = recommended_price

        elif accept == "no":

            # Let the seller choose their own price
            try:
                sell_price = float(
                    input("Enter your own selling price ($): ")
                )

                # The price must be greater than zero
                if sell_price <= 0:
                    print("Selling price must be greater than 0.")
                    continue

            except ValueError:

                # Handle invalid price input
                print("Please enter a valid price.")
                continue

        else:

            # Handle invalid yes/no answers
            print("Please enter yes or no.")
            continue

        # Show the final selling price
        print(
            "\nFinal Selling Price: $",
            round(sell_price, 2)
        )

        # Ask the seller to confirm the listing
        confirm = input(
            "Do you want to list this item? (yes/no): "
        ).lower()

        if confirm == "yes":

            # Add the item to the marketplace
            marketplace.append({
                "name": item,
                "price": sell_price,
                "condition": condition
            })

            print("Item listed successfully!")

    # =========================
    # BUY AN ITEM
    # =========================
    elif choice == "2":

        # Check if there are any items available
        if len(marketplace) == 0:
            print("\nThere are no items available.")
            continue

        print("\n--- Items for Sale ---")

        # Display all available items
        for i, item in enumerate(marketplace):

            print(
                i + 1,
                item["name"],
                "- $", round(item["price"], 2),
                "-", item["condition"]
            )

        try:
            # Ask the buyer to choose an item
            item_number = int(
                input("Choose an item to buy: ")
            )

            # Check if the item number is valid
            if item_number < 1 or item_number > len(marketplace):
                print("Invalid item number.")
                continue

            # Get the selected item
            selected_item = marketplace[item_number - 1]

            # Calculate the platform fee
            price = selected_item["price"]
            fee = price * FEE_RATE

            # Calculate how much the seller receives
            seller_receives = price - fee

            # Display the purchase information
            print("\nPurchase successful!")
            print("Item:", selected_item["name"])
            print("Price: $", round(price, 2))
            print("Platform Fee (5%): $", round(fee, 2))
            print(
                "Seller receives: $",
                round(seller_receives, 2)
            )

            # Remove the item after it is sold
            marketplace.pop(item_number - 1)

        except ValueError:

            # Handle invalid item numbers
            print("Please enter a valid number.")

    # =========================
    # SEARCH ITEMS
    # =========================
    elif choice == "3":

        # Check if there are items to search
        if len(marketplace) == 0:
            print("\nThere are no items for sale.")
            continue

        # Get the item name the user wants to search for
        search = input(
            "\nEnter item name to search: "
        ).lower()

        # Store matching items
        results = []

        # Search through all items
        for i, item in enumerate(marketplace):

            # Check if the search word is in the item name
            if search in item["name"].lower():
                results.append((i, item))

        # Show a message if nothing was found
        if len(results) == 0:
            print("No items found.")

        else:

            print("\n--- Search Results ---")

            # Display the matching items
            for number, item in results:

                print(
                    number + 1,
                    item["name"],
                    "- $", round(item["price"], 2),
                    "-", item["condition"]
                )

            # Ask if the user wants to buy an item
            buy = input(
                "\nDo you want to buy one of these items? (yes/no): "
            ).lower()

            if buy == "yes":

                try:

                    # Ask which item the user wants to buy
                    item_number = int(
                        input("Enter the item number: ")
                    )

                    # Check if the item number is valid
                    if item_number < 1 or item_number > len(marketplace):
                        print("Invalid item number.")
                        continue

                    # Get the selected item
                    selected_item = marketplace[item_number - 1]

                    # Calculate the platform fee
                    price = selected_item["price"]
                    fee = price * FEE_RATE
                    seller_receives = price - fee

                    # Display purchase information
                    print("\nPurchase successful!")
                    print("Item:", selected_item["name"])
                    print("Price: $", round(price, 2))
                    print(
                        "Platform Fee (5%): $",
                        round(fee, 2)
                    )
                    print(
                        "Seller receives: $",
                        round(seller_receives, 2)
                    )

                    # Remove the item after it is sold
                    marketplace.pop(item_number - 1)

                except ValueError:

                    print("Please enter a valid number.")

    # =========================
    # VIEW ALL ITEMS
    # =========================
    elif choice == "4":

        # Check if the marketplace is empty
        if len(marketplace) == 0:
            print("\nThere are no items for sale.")

        else:

            print("\n--- Items for Sale ---")

            # Display all items
            for i, item in enumerate(marketplace):

                print(
                    i + 1,
                    item["name"],
                    "- $", round(item["price"], 2),
                    "-", item["condition"]
                )

    # =========================
    # QUIT PROGRAM
    # =========================
    elif choice == "5":

        print(
            "\nThank you for using the marketplace!"
        )

        # Exit the while loop
        break

    else:

        # Handle an invalid menu choice
        print("Invalid choice. Please try again.")

# Display goodbye message
print("\nGoodbye!")