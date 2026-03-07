import logging

from config import INPUT_FILE, OUTPUT_FILE, LOG_FILE
from data_loader import load_sales_data
from data_processor import process_sales_data
from report_generator import generate_excel_report


def setup_logging():
    """
    Configure logging settings.
    """
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main():
    """
    Main execution pipeline for the sales automation system.
    """
    try:
        logging.info("Automation process started.")

        # Step 1: Load data
        sales_df = load_sales_data(str(INPUT_FILE))

        # Step 2: Process data
        processed_data = process_sales_data(sales_df)

        # Step 3: Generate report
        generate_excel_report(str(OUTPUT_FILE), processed_data)

        logging.info("Automation process completed successfully.")
        print("Report generated successfully.")

    except Exception as e:
        logging.error(f"Automation process failed: {e}")
        print("An error occurred. Check the log file for details.")


if __name__ == "__main__":
    setup_logging()
    main()