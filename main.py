from __future__ import annotations

from pathlib import Path

from utils import read_csv, summarize, write_json, write_report_csv


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    input_file = base_dir / "sample_data" / "input.csv"

    out_dir = base_dir / "output"
    out_csv = out_dir / "report.csv"
    out_json = out_dir / "summary.json"

    records = read_csv(input_file)

    # Simple normalization: sort by status then amount desc
    records_sorted = sorted(records, key=lambda r: (r.status, -r.amount))

    write_report_csv(out_csv, records_sorted)
    summary = summarize(records_sorted)
    write_json(out_json, summary)

    print("Done.")
    print(f"- CSV report: {out_csv}")
    print(f"- JSON summary: {out_json}")


if __name__ == "__main__":
    main()
