# Second-Hand Marketplace V3

print("Welcome to the Second-Hand Marketplace")

FEE_RATE = 0.05
marketplace = []

while True:

    print("\n--- Main Menu ---")
    print("1. Sell an item")
    print("2. Buy an item")
    print("3. Search items")
    print("4. View items")
    print("5. Quit")

    choice = input("Choose an option: ")

    # SELL
    if choice == "1":

        item = input("\nEnter item name: ")
        price = float(input("Enter original price ($): "))
        condition = input("Enter condition (new/good/fair/poor): ").lower()

        # Recommend a selling price
        if condition == "new":
            sell_price = price * 0.8
        elif condition == "good":
            sell_price = price * 0.6
        elif condition == "fair":
            sell_price = price * 0.4
        elif condition == "poor":
            sell_price = price * 0.2
        else:
            print("Invalid condition. Please try again.")
            continue

        print("\nItem:", item)
        print("Original Price: $", round(price, 2))
        print("Recommended Selling Price: $", round(sell_price, 2))

        confirm = input("Do you want to list this item? (yes/no): ").lower()

        if confirm == "yes":

            marketplace.append({
                "name": item,
                "price": sell_price,
                "condition": condition
            })

            print("Item listed successfully!")

    # BUY
    elif choice == "2":

        if len(marketplace) == 0:
            print("\nThere are no items available.")
            continue

        print("\n--- Items for Sale ---")

        for i, item in enumerate(marketplace):
            print(
                i + 1,
                item["name"],
                "- $", round(item["price"], 2),
                "-", item["condition"]
            )

        try:
            item_number = int(input("Choose an item to buy: "))

            if item_number < 1 or item_number > len(marketplace):
                print("Invalid item number.")
                continue

            selected_item = marketplace[item_number - 1]

            price = selected_item["price"]
            fee = price * FEE_RATE
            seller_receives = price - fee

            print("\nPurchase successful!")
            print("Item:", selected_item["name"])
            print("Price: $", round(price, 2))
            print("Platform Fee (5%): $", round(fee, 2))
            print("Seller receives: $", round(seller_receives, 2))

            marketplace.pop(item_number - 1)

        except ValueError:
            print("Please enter a valid number.")

    # SEARCH ITEMS
    elif choice == "3":

        if len(marketplace) == 0:
            print("\nThere are no items for sale.")
            continue

        search = input("\nEnter item name to search: ").lower()

        results = []

        for i, item in enumerate(marketplace):
            if search in item["name"].lower():
                results.append((i, item))

        if len(results) == 0:
            print("No items found.")
        else:
            print("\n--- Search Results ---")

            for number, item in results:
                print(
                    number + 1,
                    item["name"],
                    "- $", round(item["price"], 2),
                    "-", item["condition"]
                )

            buy = input("\nDo you want to buy one of these items? (yes/no): ").lower()

            if buy == "yes":

                try:
                    item_number = int(input("Enter the item number: "))

                    if item_number < 1 or item_number > len(marketplace):
                        print("Invalid item number.")
                        continue

                    selected_item = marketplace[item_number - 1]

                    price = selected_item["price"]
                    fee = price * FEE_RATE
                    seller_receives = price - fee

                    print("\nPurchase successful!")
                    print("Item:", selected_item["name"])
                    print("Price: $", round(price, 2))
                    print("Platform Fee (5%): $", round(fee, 2))
                    print("Seller receives: $", round(seller_receives, 2))

                    marketplace.pop(item_number - 1)

                except ValueError:
                    print("Please enter a valid number.")

    # VIEW ITEMS
    elif choice == "4":

        if len(marketplace) == 0:
            print("\nThere are no items for sale.")
        else:
            print("\n--- Items for Sale ---")

            for i, item in enumerate(marketplace):
                print(
                    i + 1,
                    item["name"],
                    "- $", round(item["price"], 2),
                    "-", item["condition"]
                )

    # QUIT
    elif choice == "5":
        print("\nThank you for using the marketplace!")
        break

    else:
        print("Invalid choice. Please try again.")

print("\nGoodbye!")
