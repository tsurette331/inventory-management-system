SELECT *
FROM Inventory;

SELECT item_name, quantity, reorder_point
FROM Inventory;

--low stock items
SELECT item_name, quantity, reorder_point
FROM Inventory
WHERE quantity < reorder_point;

--out of stock
SELECT item_name
FROM Inventory
WHERE quantity = 0;

--with supplier
SELECT 
    i.item_name,
    i.quantity,
    s.supplier_name
FROM Inventory i
JOIN Supplier s ON i.supplier_id = s.supplier_id;