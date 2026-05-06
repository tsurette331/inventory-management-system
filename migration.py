from db import cursor, conn

# Rename columns
cursor.execute("UPDATE Inventory SET status = 'In Stock' WHERE status = 'Available';")

conn.commit()

print("status updated successfully.")