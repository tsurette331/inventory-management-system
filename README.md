# Inventory Management System

A CLI-based inventory tracking system that simulates real-world business operations, including product management, supplier relationships, and stock monitoring using a relational database.

---

## System Design Highlights

- Designed a normalized relational database with primary and foreign key relationships  
- Implemented full CRUD operations for inventory management  
- Applied layered architecture separating UI, business logic, and data access  
- Enforced business rules such as reorder point thresholds and stock status updates  
- Built input validation to ensure data integrity and prevent invalid operations  

---

## Features

- View full inventory  
- Add new products  
- Update product quantities  
- Delete products  
- Identify low-stock items using reorder points  
- Search inventory by product name  
- Assign suppliers and locations  

---

## Tech Stack

- Python  
- SQLite  
- SQL (joins, filtering, CRUD operations)

---

## System Architecture

```text
User (CLI Interface)
   ↓
app.py (Controller Layer)
   ↓
inventory.py (Business Logic Layer)
   ↓
db.py (Database Access Layer)
   ↓
SQLite Database
```

---

## Database Design

**Inventory**
- product_id (PK)
- product_name 
- quantity  
- reorder_point  
- status  
- supplier_id (FK → Supplier.supplier_id)
- location_id (FK → Location.location_id)

**Supplier**
- supplier_id (PK)
- supplier_name  

**Location**
- location_id (PK)
- location_name  

---

## Example Output

```text
Product: Reagent X | Qty: 50 | Supplier: PharmaSupply Co
Product: Test Kit A | Qty: 10 | Supplier: BioLab Inc
```

---

## UI Prototype

View Figma Prototype (ADD LINK)

Simple interface showing how users interact with the system.

---

## How to Run

```bash
python app.py
```

---

## Documentation

Full Business & Technical Design Document included in this repository.

---

## Author

Tom Surette

