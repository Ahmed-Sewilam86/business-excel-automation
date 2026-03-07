import pandas as pd
import logging


REQUIRED_COLUMNS = [
    "Order ID",
    "Date",
    "Product",
    "Quantity",
    "Price",
    "Country"
]


def load_sales_data(file_path: str) -> pd.DataFrame:
    """
    Load sales data from an Excel file and validate required columns.

    Args:
        file_path (str): Path to the input Excel file.

    Returns:
        pd.DataFrame: Validated sales data.
    """
    try:
        df = pd.read_excel(file_path)

        missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        logging.info("Sales data loaded successfully.")
        return df

    except Exception as e:
        logging.error(f"Error loading sales data: {e}")
        raise