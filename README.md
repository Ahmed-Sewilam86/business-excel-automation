# Business Excel Automation System

A Python automation tool that transforms raw sales data into 
a formatted, multi-sheet Excel report — automatically.

---

## The Problem It Solves

Many businesses track sales in messy Excel files with no 
structure or summaries. This tool takes that raw data and 
produces a clean, professional report in seconds.

---

## What It Does

- Loads raw sales data from Excel
- Validates data structure automatically
- Cleans and processes the data
- Calculates key business metrics:
  - Total revenue
  - Revenue by product
  - Revenue by country
  - Monthly revenue trends
- Generates a formatted Excel report with 4 sheets
- Logs all operations for traceability

---

## Output Preview

| Sheet Name         | Description                        |
|--------------------|------------------------------------|
| Clean Data         | Validated and processed records    |
| Revenue by Product | Sales breakdown per product        |
| Revenue by Country | Sales breakdown per country        |
| Monthly Revenue    | Month-by-month revenue trends      |

---

## Project Structure
```
business-excel-automation/
│
├── main.py                  # Main execution pipeline
├── config.py                # File paths configuration
├── data_loader.py           # Data loading and validation
├── data_processor.py        # Data cleaning and metrics
├── report_generator.py      # Excel report generation
├── generate_sample_data.py  # Sample data generator
├── requirements.txt         # Project dependencies
└── sample_data/
    └── sales_raw.xlsx       # Input data file
```

---

## Technologies Used

- Python 3.10+
- pandas
- openpyxl

---

## Installation
```bash
git clone https://github.com/your-username/business-excel-automation.git
cd business-excel-automation
pip install -r requirements.txt
```

---

## How to Run

**Step 1 — Generate sample data:**
```bash
python generate_sample_data.py
```

**Step 2 — Run the automation:**
```bash
python main.py
```

**Step 3 — Open your report:**

The file `sales_report.xlsx` will be created in the project folder.

---

## Use Cases

- Small business sales reporting
- Monthly performance tracking
- Multi-product revenue analysis
- Country-level sales breakdown

---

## License

MIT License — free to use and modify.