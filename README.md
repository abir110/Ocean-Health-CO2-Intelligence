# Ocean & Atmosphere: CO₂ Intelligence Brief

> Prepared as a data analysis brief for a wildlife documentary production team — tracking 125 years of global CO₂ emissions to identify the regions and decades most critical to the planet's climate story.

## The Brief

Imagine being handed this task: *"We're filming a documentary on climate change. Show us, with data, how the planet got here — and where the story needs to focus."*

This project answers that brief using 125 years of CO₂ emissions data (1900–2024) across 185 countries.

## Key Findings

- **Global emissions grew 14x** since 1900 — from 24 billion tonnes (1900s) to 342 billion tonnes (2010s)
- **The tipping point was 1950–1970** — emissions grew faster in these two decades than in the previous 50 years combined
- **The United States is the largest historical emitter** (424.85B tonnes since 1900), but **China overtook it around 2006** and now emits over 2x more annually
- **The UK cut emissions by 42.7%** since 2000 — proof that large economies can reduce emissions while growing
- **2020 saw a rare dip** (181B tonnes) due to global lockdowns — showing how quickly emissions can fall when human activity changes

## Dashboard

![Dashboard Preview](dashboard-prewier.PNG)

The interactive Power BI dashboard includes:
- Global CO₂ trend (1900–2024)
- USA vs China emissions race
- Top 10 historical emitters
- Emissions by decade

## Tools & Skills Used

| Tool | Purpose |
|------|---------|
| Python (pandas) | Data cleaning, transformation |
| SQL (SQLite) | Business question analysis |
| Power BI | Interactive dashboard |

## Project Structure
ocean-health-project/
├── data/                          # Raw CO2 dataset (OWID)
├── output/                        # Cleaned data, SQL exports, dashboard
├── clean.py                       # Data cleaning script
├── analyse.py                     # Python analysis
├── load_sql.py                    # Load data into SQLite
├── export_sql.py                  # SQL business queries
└── ocean_health_dashboard.pbix    # Power BI dashboard

## Data Source

[Our World in Data — CO₂ and Greenhouse Gas Emissions](https://ourworldindata.org/co2-emissions)

## Author

Built as part of a data analytics portfolio focused on environmental intelligence and sustainability reporting.
