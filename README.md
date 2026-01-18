# python-process-automation

Simple Python automation project for CSV processing and reporting

## Overview

This project demonstrates clean Python code organization and data processing fundamentals:

- CSV file reading with validation
- Data transformation and summarization
- Multiple output formats (CSV + JSON)
- Proper error handling
- Type hints and modern Python features

## Features

- ✅ Reads CSV data with validation
- ✅ Summarizes records by status (paid, pending, failed)
- ✅ Generates sorted CSV report
- ✅ Produces JSON summary with statistics
- ✅ Stdlib-only (no external dependencies)

## Project Structure

```
python-process-automation/
├── README.md
├── requirements.txt        # Stdlib only
├── main.py                 # Entry point
├── utils.py                # Data processing logic
└── sample_data/
    └── input.csv           # Sample input data
```

## Usage

```bash
python main.py
```

Outputs:
- `output/report.csv` - Sorted CSV report
- `output/summary.json` - Statistics summary

## Requirements

- Python 3.11+
- No external dependencies (stdlib only)

## Example Output

**Summary (output/summary.json):**
```json
{
  "count": 4,
  "total_amount": 450.50,
  "average_amount": 112.62,
  "by_status_count": {
    "paid": 2,
    "pending": 1,
    "failed": 1
  },
  "by_status_amount": {
    "paid": 320.50,
    "pending": 80.00,
    "failed": 50.00
  }
}
```
