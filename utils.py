from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Record:
    name: str
    email: str
    amount: float
    status: str


VALID_STATUSES = {"paid", "pending", "failed"}


def read_csv(path: Path) -> list[Record]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    records: list[Record] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {"name", "email", "amount", "status"}
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"CSV must contain columns: {sorted(required)}")

        for i, row in enumerate(reader, start=2):
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip().lower()
            status = (row.get("status") or "").strip().lower()
            amount_raw = (row.get("amount") or "").strip()

            if not name or not email:
                raise ValueError(f"Invalid row {i}: name/email required")

            try:
                amount = float(amount_raw)
            except ValueError as e:
                raise ValueError(f"Invalid row {i}: amount must be numeric") from e

            if status not in VALID_STATUSES:
                raise ValueError(f"Invalid row {i}: status must be one of {sorted(VALID_STATUSES)}")

            records.append(Record(name=name, email=email, amount=amount, status=status))

    return records


def summarize(records: Iterable[Record]) -> dict:
    total = 0.0
    by_status: dict[str, int] = {s: 0 for s in VALID_STATUSES}
    by_status_amount: dict[str, float] = {s: 0.0 for s in VALID_STATUSES}

    count = 0
    for r in records:
        count += 1
        total += r.amount
        by_status[r.status] += 1
        by_status_amount[r.status] += r.amount

    avg = (total / count) if count else 0.0

    return {
        "count": count,
        "total_amount": round(total, 2),
        "average_amount": round(avg, 2),
        "by_status_count": by_status,
        "by_status_amount": {k: round(v, 2) for k, v in by_status_amount.items()},
    }


def write_report_csv(path: Path, records: list[Record]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "email", "amount", "status"])
        for r in records:
            writer.writerow([r.name, r.email, f"{r.amount:.2f}", r.status])


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
