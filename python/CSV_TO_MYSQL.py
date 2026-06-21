import pandas as pd
import mysql.connector

df = pd.read_csv("data/cleaned_placement_data.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="placement_db"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO placement_data
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()