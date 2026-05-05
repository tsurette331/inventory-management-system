from db import cursor, conn
from utils import get_int, get_non_empty

def view_inventory():
    cursor.execute("SELECT * FROM Inventory;")
    rows = cursor.fetchall()
    
    #for row in rows:
        #print(f"Product: {row[1]} | Qty: {row[2]}")

def low_stock_items():
    cursor.execute("""
        SELECT item_name, quantity, reorder_point
        FROM Inventory
        WHERE quantity <= reorder_point
        """)
    rows = cursor.fetchall()
    print("Low Stock Items: ")
    for row in rows:
        print(f"Product: {row[0]} | Qty: {row[1]} | RO Point: {row[2]}")

def inventory_with_suppliers():
    cursor.execute("""
        SELECT i.item_name, i.quantity, s.supplier_name
        FROM Inventory i
        JOIN Supplier s ON i.supplier_id = s.supplier_id;
    """)
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"Product: {row[0]} | Qty: {row[1]} | Supplier: {row[2]}")

def search_by_product():
    keyword = input("Search inventory by product: ")
    cursor.execute("""
        SELECT item_name, quantity, reorder_point
        FROM Inventory
        WHERE item_name LIKE ?
        """, ("%" + keyword + "%",))

    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No matching results.")
    else:
        for row in rows:
            print(f"Product: {row[0]} | Qty: {row[1]} | RO Point: {row[2]}")

def select_supplier():
    while True:
        cursor.execute("SELECT supplier_id, supplier_name FROM Supplier")
        suppliers = cursor.fetchall()
        supplier_ids = [s[0] for s in suppliers]
        
        print("Suppliers:")
        for s in suppliers:
            print(f"{s[0]}. {s[1]}")

        print("\nOptions:")
        print("A - Add new supplier")
        print("Q - Cancel")

        choice = input("Enter supplier ID or choose an option: ").strip()

        if choice.lower() == 'q':
            print("Exiting program.")
            return None

        if choice.lower() == 'a':
            add_supplier()
            continue
    
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input.")
            continue
    
        if choice in supplier_ids:
            return choice
        else:
            print("Invalid supplier ID.")

def select_location():
    cursor.execute("SELECT location_id, location_name FROM Location")
    locations = cursor.fetchall()
    location_ids = [l[0] for l in locations]

    while True:
        print("Locations:")
        for l in locations:
            print(f"{l[0]}. {l[1]}")

        choice = input("Enter location ID or type 'q' to exit: ")

        if choice.lower() == 'q':
            print("Exiting program.")
            return None
        
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
    
        if choice in location_ids:
            return choice
        else:
            print("Invalid location ID.")

def add_product():
    new_product = get_non_empty("Add product: ")
    new_qty = get_int("Add Quantity: ")
    new_ro = get_int("Add Reorder Point: ")
    supplier_id = select_supplier()
    if supplier_id is None:
        return
    location_id = select_location()
    if location_id is None:
        return

    if new_qty <= new_ro:
        status = "Low Stock"
    else:
        status = "In Stock"
    
    cursor.execute("""
    INSERT INTO Inventory 
    (item_name, quantity, reorder_point, supplier_id, location_id, status)
    VALUES ( ?, ?, ?, ?, ?, ?)
    """, (new_product, new_qty, new_ro, supplier_id, location_id, status))

    conn.commit()

    print("Product Added Successfully!")

def add_supplier():
    new_supplier = get_non_empty("Enter new supplier: ")

    cursor.execute("""
    INSERT INTO Supplier
    (supplier_name)
    VALUES (?)
    """, (new_supplier,))

    conn.commit()

    print("Supplier added successfully!")

def delete_product():
    deleted_product = get_non_empty("Enter the product name to be deleted: ")

    cursor.execute("""
        SELECT * FROM Inventory WHERE item_name = ?
    """, (deleted_product,))

    if cursor.fetchone() is None:
        print("Product not found.")
        return

    confirm = input(f"Delete '{deleted_product}'? (y/n): ")

    if confirm.lower() != 'y':
        print("Delete cancelled.")
        return

    cursor.execute("""
    DELETE FROM Inventory
    WHERE item_name = ?
    """, (deleted_product,))

    conn.commit()

    print("Product Successfully Deleted!")

def update_qty():
    product_name = get_non_empty("Enter the product you want to update: ")
    new_qty = get_int("Enter updated quantity: ")

    cursor.execute("""
        SELECT reorder_point 
        FROM Inventory 
        WHERE item_name = ?
    """, (product_name,))

    result = cursor.fetchone()

    if result is None:
        print("Product not found.")
        return

    reorder_point = result[0]
    
    if new_qty <= reorder_point:
        status = "low stock"
    else:
        status = "in stock"
    
    cursor.execute("""
    UPDATE Inventory
    SET quantity = ?, status = ?
    WHERE item_name = ?
    """, (new_qty, status, product_name))

    conn.commit()

    print("Quantity Successfully Updated!")