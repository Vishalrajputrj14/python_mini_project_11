menu = {
    "Pizza": 199,
    "Pasta": 139,
    "Burger": 69,
    "Salad": 30,
    "Cold Coffee": 120,
    "Coffee": 20,
    "Patties": 49
}

print("Welcome to Python Restaurant")
print("Pizza : Rs199\nPasta : Rs139\nBurger : Rs69\nSalad : Rs30\nCold Coffee : Rs120\nCoffee : Rs20\nPatties : Rs49")

order_total = 0

item_1 = input("Enter the name of item you want to order: ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order")
else:
    print("Item not available")

another_order = input("Do you want to add another item? (yes/no): ").lower()

if another_order == "yes":
    item_2 = input("Enter second item: ").title()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order")
    else:
        print("Item not available")

print(f"Total bill = Rs {order_total}")