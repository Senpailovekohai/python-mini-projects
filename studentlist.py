ITEMS = [
    ["Water",  0.50, 3],
    ["Juice",  1.20, 2],
    ["Chips",  0.80, 1],
    ["Coffee", 1.50, 2],
]

balance = 0.0
selected = None


def show_menu():
    print("\n--- Vending Machine ---")
    print(f"Balance: ${balance:.2f}")
    print("\nItems:")
    for i, item in enumerate(ITEMS):
        print(f"  {i+1}. {item[0]} - ${item[1]:.2f} (stock: {item[2]})")
    print("\nActions: insert / select / cancel")


while True:
    show_menu()
    action = input("Action: ").strip().lower()

    if action == "cancel":
        if balance > 0:
            print(f"Refund: ${balance:.2f}")
        print("Goodbye!")
        break

    elif action == "insert":
        while True:
            try:
                coin = float(input("Insert coin amount: $"))
                if coin <= 0:
                    print("Please insert a positive amount.")
                    continue
                break
            except ValueError:
                print("Numbers only please.")
        balance += coin
        print(f"Balance is now: ${balance:.2f}")

    elif action == "select":
        while True:
            try:
                choice = int(input("Enter item number: "))
                if 1 <= choice <= len(ITEMS):
                    break
                print(f"Please enter a number between 1 and {len(ITEMS)}.")
            except ValueError:
                print("Numbers only please.")

        selected = choice - 1  # convert to list index

        # Check stock FIRST (as per flowchart)
        if ITEMS[selected][2] <= 0:
            print(f"Sorry, {ITEMS[selected][0]} is out of stock.")

        # Then check balance
        elif balance < ITEMS[selected][1]:
            shortfall = ITEMS[selected][1] - balance
            print(f"Not enough balance. You need ${shortfall:.2f} more.")

        # All good — dispense
        else:
            print(f"\n✓ Dispensing {ITEMS[selected][0]}...")
            ITEMS[selected][2] -= 1  # decrement stock

            if balance > ITEMS[selected][1]:
                change = balance - ITEMS[selected][1]
                print(f"Change returned: ${change:.2f}")

            balance = 0.0
            print("Thank you! Come again.")
            break

    else:
        print("Invalid action. Type insert, select, or cancel.")