CREATE TABLE Inventory (
    inventory_id INTEGER PRIMARY KEY,
    item_name TEXT,
    quantity INTEGER,
    reorder_point INTEGER,
    status TEXT,
    supplier_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);

CREATE TABLE Location (
    location_id INTEGER PRIMARY KEY,
    location_name TEXT
);

CREATE TABLE Supplier (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT
);