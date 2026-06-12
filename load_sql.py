import pandas as pd
import sqlite3

conn = sqlite3.connect("output/ocean_health.db")

df = pd.read_csv("output/co2_clean.csv")

df.to_sql("co2_emissions", conn, if_exists="replace", index=False)

print("Database created!")
print("Rows:", pd.read_sql("SELECT COUNT(*) as total FROM co2_emissions", conn).iloc[0,0])

conn.close()