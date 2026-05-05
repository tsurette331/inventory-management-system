import sqlite3

conn = sqlite3.connect("database/inventory.db")
cursor = conn.cursor()