INSERT INTO Supplier (supplier_id, supplier_name) VALUES
(1, 'PharmaSupply Co'),
(2, 'BioLab Inc'),
(3, 'MedChem Solutions'),
(4, 'LabSource LLC');

INSERT INTO Location (location_id, location_name) VALUES
(1, 'Warehouse A'),
(2, 'Warehouse B'),
(3, 'Cold Storage'),
(4, 'Lab Storage');

INSERT INTO Inventory (inventory_id, item_name, quantity, reorder_point, status, supplier_id, location_id) VALUES
(1, 'Reagent X', 50, 20, 'In Stock', 1, 1),
(2, 'Test Kit A', 10, 15, 'Low Stock', 2, 2),
(3, 'Buffer Solution B', 0, 10, 'Out of Stock', 3, 3),
(4, 'Chemical Compound C', 75, 30, 'In Stock', 1, 1),
(5, 'Diagnostic Kit D', 5, 10, 'Low Stock', 2, 4),
(6, 'Enzyme Mix E', 100, 40, 'In Stock', 4, 2),
(7, 'Culture Media F', 20, 25, 'Low Stock', 3, 3),
(8, 'Protein Sample G', 60, 20, 'In Stock', 1, 4),
(9, 'Antibody H', 8, 12, 'Low Stock', 2, 1),
(10, 'Solvent I', 200, 50, 'In Stock', 4, 2),
(11, 'Vaccine Component J', 0, 25, 'Out of Stock', 3, 3),
(12, 'Lab Kit K', 30, 10, 'In Stock', 2, 4),
(13, 'pH Buffer L', 12, 15, 'Low Stock', 1, 1),
(14, 'Growth Factor M', 90, 30, 'In Stock', 4, 2),
(15, 'Sterile Filter N', 3, 10, 'Low Stock', 3, 3);