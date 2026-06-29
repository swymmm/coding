#Inventory: Create inventory dict (item → quantity). Write functions: add_item, remove_item, check_stock, display_all.
inventory={
    "milk": 10,
    "eggs": 20,
    "bread": 15,
    "butter": 8
}

def add_item(item, quantity):
    if item in inventory:
        inventory[item]+=quantity
    else:
        inventory[item]=quantity

def remove_item(item, quantity):
    if item not in inventory:
        print(f"the {item} is not found in inventory")
    elif inventory[item]<quantity:
        print(f"not enough stock. available: {inventory[item]}")
    else:
        inventory[item]-=quantity
        print(f"{item} updated.Remaining: {inventory[item]}")

def check_stock(item):
    if item in inventory:
        print(f"{item}: {inventory[item]} units.")
    else:
        print(f"{item} not found")

def display_all():
    print("\n--------inventory-----------")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print("------------------------------")

display_all()
add_item("apple", 10)
remove_item("bread", 2)
check_stock("milk")
display_all()