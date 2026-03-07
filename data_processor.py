import pandas as pd
import logging


def process_sales_data(df: pd.DataFrame) -> dict:
    """
    Process sales data and calculate key business metrics.

    Args:
        df (pd.DataFrame): Raw sales data.

    Returns:
        dict: Dictionary containing processed metrics.
    """
    try:
        # Ensure correct data types
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

        # Drop rows with critical missing values
        df = df.dropna(subset=["Date", "Quantity", "Price"])

        # Create revenue column
        df["Revenue"] = df["Quantity"] * df["Price"]

        # Total revenue
        total_revenue = df["Revenue"].sum()

        # Revenue by product
        revenue_by_product = (
            df.groupby("Product")["Revenue"]
            .sum()
            .reset_index()
            .sort_values(by="Revenue", ascending=False)
        )

        # Revenue by country
        revenue_by_country = (
            df.groupby("Country")["Revenue"]
            .sum()
            .reset_index()
            .sort_values(by="Revenue", ascending=False)
        )

        # Monthly revenue
        df["Month"] = df["Date"].dt.to_period("M").astype(str)
        monthly_revenue = (
            df.groupby("Month")["Revenue"]
            .sum()
            .reset_index()
        )

        logging.info("Sales data processed successfully.")

        return {
            "clean_data": df,
            "total_revenue": total_revenue,
            "revenue_by_product": revenue_by_product,
            "revenue_by_country": revenue_by_country,
            "monthly_revenue": monthly_revenue,
        }

    except Exception as e:
        logging.error(f"Error processing sales data: {e}")
        raise