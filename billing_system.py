# Aradhya's Billing System

items = {
    "rice": 50,
    "sugar": 40,
    "milk": 30,
    "bread": 25,
    "cheese": 150,
    "yogurt": 45
}

def calculate_bill():
    total = 0
    bill_items = {}

    print("Welcome to Aradhya's Billing System\n")

    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").lower()

        if item_name == "done":
            break

        if item_name in items:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.\n")
                    continue
            except ValueError:
                print("Please enter a valid number.\n")
                continue

            bill_items[item_name] = bill_items.get(item_name, 0) + quantity
            item_total = items[item_name] * quantity
            total += item_total
            print(f"Added {quantity} x {item_name} = {item_total}\n")
        else:
            print("Item not found. Please enter a valid item.\n")

    # Print formatted bill
    print("\n--- BILL DETAILS ---")
    print("Item".ljust(10), "Qty".rjust(5), "Price".rjust(10))
    for item, qty in bill_items.items():
        print(item.ljust(10), str(qty).rjust(5), str(items[item] * qty).rjust(10))

    print("\nTotal bill amount: ", total)

    # Optional: save bill to a file
    with open("bill.txt", "w") as f:
        f.write("--- BILL DETAILS ---\n")
        f.write("Item".ljust(10) + "Qty".rjust(5) + "Price".rjust(10) + "\n")
        for item, qty in bill_items.items():
            f.write(item.ljust(10) + str(qty).rjust(5) + str(items[item] * qty).rjust(10) + "\n")
        f.write(f"\nTotal bill amount: {total}\n")

    print("\nBill has been saved to 'bill.txt'.")

    return total

# Run the billing system
bill = calculate_bill()
