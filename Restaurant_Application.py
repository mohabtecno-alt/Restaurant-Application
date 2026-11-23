#this will be the file to build the app
"""Beginner-friendly restaurant menu, ordering, and billing application."""

# Dish name -> price (in EGP)
menu = {
    "Burger": 120.0,
    "Pizza": 180.0,
    "Pasta": 140.0,
    "Salad": 70.0,
    "Juice": 40.0,
}

# Each order item stores its dish, unit price, and quantity.
order = []

# Example tax rate: 10%. Change this value as needed.
TAX_RATE = 0.10


def get_positive_number(message, whole_number=False):
    """Ask again until the user enters a number greater than zero."""
    while True:
        try:
            value = int(input(message)) if whole_number else float(input(message))
            if 0 < value < float("inf"):
                return value
        except ValueError:
            pass
        print("Please enter a valid positive number.")


def view_menu():
    print("\n--- RESTAURANT MENU ---")
    if not menu:
        print("The menu is empty.")
        return

    for number, (dish, price) in enumerate(menu.items(), start=1):
        print(f"{number}. {dish} - {price:.2f} EGP")


def add_to_order():
    if not menu:
        print("No dishes are currently available.")
        return

    view_menu()
    choice = get_positive_number("Enter dish number: ", whole_number=True)
    dishes = list(menu.items())

    if choice > len(dishes):
        print("That dish number is not on the menu.")
        return

    dish, price = dishes[choice - 1]
    quantity = get_positive_number("Enter quantity: ", whole_number=True)
    order.append({"dish": dish, "price": price, "quantity": quantity})
    print(f"Added {quantity} x {dish} to your order!")


def generate_bill():
    if not order:
        print("\nYour order is empty. Please add a dish first.")
        return

    print("\n========== YOUR BILL ==========")
    subtotal = 0

    for item in order:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total
        print(f'{item["dish"]} x {item["quantity"]}: {item_total:.2f} EGP')

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print("-------------------------------")
    print(f"Subtotal: {subtotal:.2f} EGP")
    print(f"Tax ({TAX_RATE * 100:g}%): {tax:.2f} EGP")
    print(f"Total: {total:.2f} EGP")
    print("===============================")


def update_menu():
    print("\n--- UPDATE MENU (ADMIN) ---")
    print("1. Add a dish")
    print("2. Remove a dish")
    print("3. Return to main menu")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        dish = input("Enter the dish name: ").strip().title()
        if not dish:
            print("Dish name cannot be empty.")
        elif dish in menu:
            print("That dish is already on the menu.")
        else:
            price = get_positive_number("Enter the price (EGP): ")
            menu[dish] = price
            print(f"{dish} added to the menu!")
    elif choice == "2":
        view_menu()
        if menu:
            dish = input("Enter the name of the dish to remove: ").strip().title()
            if dish in menu:
                del menu[dish]
                print(f"{dish} removed from the menu!")
            else:
                print("Dish not found.")
    elif choice == "3":
        return
    else:
        print("Invalid option.")


def main():
    while True:
        print("\n===== RESTAURANT SYSTEM =====")
        print("1. View Menu")
        print("2. Add to Order")
        print("3. Generate Bill")
        print("4. Update Menu (Admin)")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            view_menu()
        elif choice == "2":
            add_to_order()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            update_menu()
        elif choice == "5":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
