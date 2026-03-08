import sys
from pathlib import Path

# Handle both normal Python and PyInstaller exe
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "sample_data" / "sales_raw.xlsx"
OUTPUT_FILE = BASE_DIR / "sales_report.xlsx"
LOG_FILE = BASE_DIR / "automation.log"