menu = {
    "Burger": 120,
    "Pizza": 180,
    "Pasta": 140,
    "Salad": 70,
    "Juice": 40,
}


order = []


TAX_RATE = 0.10

def view_menu():
    print("\n___ RESTAURANT MENU ___")
    if not menu:
        print("The menu is empty.")
        return

    number = 1

    for dish in menu:
        price = menu[dish]
        print(number, dish, "-", price, "EGP")
        number += 1


def add_to_order():
    if not menu:
        print("No dishes are currently available.")
        return

    view_menu()
    choice = int(input("Enter dish number: "))
    dishes = list(menu.items())

    if choice > len(dishes):
        print("That dish number is not on the menu.")
        return

    dish, price = dishes[choice - 1]
    quantity = int(input("Enter quantity: "))
    order.append({"dish": dish, "price": price, "quantity": quantity})
    print(f"Added {quantity} x {dish} to your order!")


def generate_bill():
    if not order:
        print("\nYour order is empty. Please add a dish first.")
        return

    print("\n_____________ YOUR BILL _____________")
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
    print("________________________________")


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
            price = ("Enter the price (EGP): ")
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
        print("\n_________ RESTAURANT SYSTEM __________")
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
