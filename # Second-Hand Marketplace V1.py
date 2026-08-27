#Second-Hand Marketplace V1

print("Welcome to the Second-Hand Marketplace")

while True:

    # Get item information
    item = input("\nEnter item name (or type 'quit' to exit): ")

    if item.lower() == "quit":
        print("Thank you for using the marketplace!")
        break

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

    # Show result
    print("\nItem:", item)
    print("Original Price: $", price)
    print("Recommended Selling Price: $", round(sell_price, 2))

print("\nGoodbye!")