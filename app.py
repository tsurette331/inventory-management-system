import inventory

menu_choices = {
    "1": inventory.view_inventory,
    "2": inventory.low_stock_items,
    "3": inventory.inventory_with_suppliers,
    "4": inventory.search_by_product,
    "5": inventory.add_product,
    "6": inventory.delete_product,
    "7": inventory.update_qty,
}

def menu():
    print("\nInventory System")
    print("1. View Inventory")
    print("2. Low Stock Items")
    print("3. Supplier View")
    print("4. Search By Product")
    print("5. Add Product")
    print("6. Delete Product")
    print("7. Update Quantity")
    print("8. Exit")
    
    choice = input("Enter your choice: ").strip()
    return choice

while True:
    choice = menu()

    if choice == "8":
        print("Exiting program...")
        break
    elif choice in menu_choices:
        menu_choices[choice]()
    else:
        print("Invalid choice. Please select 1-8.")
