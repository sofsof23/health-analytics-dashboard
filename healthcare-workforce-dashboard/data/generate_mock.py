"""Generate synthetic WHO-shaped data for the scaffold dashboard.

This is *mock data* — values are plausible-looking but invented.
Replace `data/mock_data.csv` with real WHO Global Health Observatory data
on Day 2 of the build plan. See `notebooks/01_eda_scaffold.ipynb`.

Usage:
    python data/generate_mock.py
"""
import csv
import random
from pathlib import Path

random.seed(42)

# (country, ISO3, WHO region, income band)
COUNTRIES = [
    # High income
    ("United States", "USA", "Americas", "high"),
    ("Canada", "CAN", "Americas", "high"),
    ("United Kingdom", "GBR", "Europe", "high"),
    ("Germany", "DEU", "Europe", "high"),
    ("France", "FRA", "Europe", "high"),
    ("Japan", "JPN", "Western Pacific", "high"),
    ("Australia", "AUS", "Western Pacific", "high"),
    ("Norway", "NOR", "Europe", "high"),
    ("Switzerland", "CHE", "Europe", "high"),
    # GCC (the comparative lens)
    ("Saudi Arabia", "SAU", "Eastern Mediterranean", "gcc"),
    ("United Arab Emirates", "ARE", "Eastern Mediterranean", "gcc"),
    ("Qatar", "QAT", "Eastern Mediterranean", "gcc"),
    ("Kuwait", "KWT", "Eastern Mediterranean", "gcc"),
    ("Bahrain", "BHR", "Eastern Mediterranean", "gcc"),
    ("Oman", "OMN", "Eastern Mediterranean", "gcc"),
    # Middle income
    ("Brazil", "BRA", "Americas", "middle"),
    ("Mexico", "MEX", "Americas", "middle"),
    ("Turkey", "TUR", "Europe", "middle"),
    ("Thailand", "THA", "South-East Asia", "middle"),
    ("Malaysia", "MYS", "Western Pacific", "middle"),
    ("South Africa", "ZAF", "Africa", "middle"),
    ("Egypt", "EGY", "Eastern Mediterranean", "middle"),
    # Low income
    ("Ethiopia", "ETH", "Africa", "low"),
    ("Bangladesh", "BGD", "South-East Asia", "low"),
    ("Nepal", "NPL", "South-East Asia", "low"),
    ("Tanzania", "TZA", "Africa", "low"),
    ("Uganda", "UGA", "Africa", "low"),
    ("Rwanda", "RWA", "Africa", "low"),
    ("Mali", "MLI", "Africa", "low"),
    ("Niger", "NER", "Africa", "low"),
]

# Plausible (min, max) ranges by income band
RANGES = {
    "high":   {"phys": (28, 45), "nurse": (80, 130), "beds": (25, 130), "life": (80, 84), "ncd": (9, 13),  "uhc": (80, 92)},
    "gcc":    {"phys": (22, 35), "nurse": (45, 80),  "beds": (12, 25),  "life": (75, 79), "ncd": (14, 22), "uhc": (68, 82)},
    "middle": {"phys": (15, 28), "nurse": (20, 45),  "beds": (10, 28),  "life": (72, 78), "ncd": (16, 22), "uhc": (55, 75)},
    "low":    {"phys": (1, 8),   "nurse": (3, 15),   "beds": (3, 15),   "life": (60, 68), "ncd": (18, 28), "uhc": (30, 55)},
}

YEARS = [2018, 2019, 2020, 2021, 2022]


def jitter(low: float, high: float, drift: float = 0.0) -> float:
    """Random value in range with optional drift across years."""
    return round(random.uniform(low, high) + drift, 1)


def main() -> None:
    rows = []
    for country, iso3, region, band in COUNTRIES:
        r = RANGES[band]
        for i, year in enumerate(YEARS):
            rows.append({
                "country": country,
                "iso3": iso3,
                "who_region": region,
                "year": year,
                "physicians_per_10k": jitter(*r["phys"], drift=i * 0.3),
                "nurses_per_10k": jitter(*r["nurse"], drift=i * 0.5),
                "hospital_beds_per_10k": jitter(*r["beds"]),
                "life_expectancy": jitter(*r["life"], drift=i * 0.1),
                "ncd_mortality_pct": jitter(*r["ncd"], drift=-i * 0.1),
                "uhc_service_coverage": jitter(*r["uhc"], drift=i * 0.4),
            })

    out = Path(__file__).parent / "mock_data.csv"
    with open(out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
