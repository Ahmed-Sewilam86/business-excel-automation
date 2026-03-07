from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "sample_data" / "sales_raw.xlsx"
OUTPUT_FILE = BASE_DIR / "sales_report.xlsx"

LOG_FILE = BASE_DIR / "automation.log"