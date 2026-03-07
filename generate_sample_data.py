import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "sample_data"
OUTPUT_FILE = OUTPUT_DIR / "sales_raw.xlsx"


PRODUCTS = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]
COUNTRIES = ["USA", "Germany", "UK", "Canada", "France"]


def generate_random_date(start_date: datetime, end_date: datetime) -> datetime:
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


def generate_sales_data(rows: int = 500) -> pd.DataFrame:
    today = datetime.today()
    start_date = datetime(today.year, 1, 1)
    end_date = today

    data = []

    for i in range(1, rows + 1):
        product = random.choice(PRODUCTS)
        quantity = random.randint(1, 5)
        price = random.randint(50, 2000)
        country = random.choice(COUNTRIES)
        date = generate_random_date(start_date, end_date)

        data.append(
            {
                "Order ID": i,
                "Date": date,
                "Product": product,
                "Quantity": quantity,
                "Price": price,
                "Country": country,
            }
        )

    return pd.DataFrame(data)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    df = generate_sales_data()
    df.to_excel(OUTPUT_FILE, index=False)

    print(f"Sample data generated at: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()