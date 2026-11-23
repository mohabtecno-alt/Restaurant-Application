menu = {
    "Burger": 120,
    "Pizza": 180,
    "Pasta": 140
}

for number, (price, dish) in enumerate(menu.items(), start=1):
    print(f"{number}. {price} - {dish} EGP")