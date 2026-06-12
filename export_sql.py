import sqlite3
import pandas as pd

conn = sqlite3.connect("output/ocean_health.db")

# Query A - Yearly totals
yearly = pd.read_sql("""
    SELECT 
        year,
        ROUND(SUM(co2_emissions) / 1000000000.0, 2) as co2_billions
    FROM co2_emissions
    WHERE LENGTH(country_code) = 3
    GROUP BY year
    ORDER BY year
""", conn)
yearly.to_csv("output/yearly_totals.csv", index=False)
print("Saved yearly_totals.csv -", yearly.shape)

# Query B - Top 10 emitters
top10 = pd.read_sql("""
    SELECT 
        country,
        ROUND(SUM(co2_emissions) / 1000000000.0, 2) as total_co2_billions
    FROM co2_emissions
    WHERE LENGTH(country_code) = 3
    GROUP BY country
    ORDER BY total_co2_billions DESC
    LIMIT 10
""", conn)
top10.to_csv("output/top10_emitters.csv", index=False)
print("Saved top10_emitters.csv -", top10.shape)

# Query C - USA vs China
usa_china = pd.read_sql("""
    SELECT 
        year,
        ROUND(SUM(CASE WHEN country = 'United States' THEN co2_emissions ELSE 0 END) / 1000000000.0, 2) as usa,
        ROUND(SUM(CASE WHEN country = 'China' THEN co2_emissions ELSE 0 END) / 1000000000.0, 2) as china
    FROM co2_emissions
    WHERE year >= 1950
    GROUP BY year
    ORDER BY year
""", conn)
usa_china.to_csv("output/usa_vs_china.csv", index=False)
print("Saved usa_vs_china.csv -", usa_china.shape)

# Query D - Emissions by decade
decade = pd.read_sql("""
    SELECT 
        (year / 10) * 10 as decade,
        ROUND(SUM(co2_emissions) / 1000000000.0, 2) as co2_billions
    FROM co2_emissions
    WHERE LENGTH(country_code) = 3
    GROUP BY decade
    ORDER BY decade
""", conn)
decade.to_csv("output/emissions_by_decade.csv", index=False)
print("Saved emissions_by_decade.csv -", decade.shape)

conn.close()
print("\nAll 4 files saved correctly!")