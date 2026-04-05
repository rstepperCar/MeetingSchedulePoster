import csv
from datetime import datetime
from meeting.models import Meeting


def load_meetings(filepath: str) -> list[Meeting]:
    """
    Read a CSV schedule file and return a list of Meeting objects.

    Expected CSV columns: Date, Family, Address, Contact Info
    Handles:
    - Normal meetings (family name + address)
    - Canceled rows (family contains "canceled")
    - Empty rows (all fields blank)
    - Multi-line addresses (handled automatically by csv module)
    """
    meetings = []

    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date_str = row["Date"].strip()
            family = row["Family"].strip()
            address = row["Address"].strip()
            contact = row["Contact Info"].strip()

            # Skip rows with no date at all
            if not date_str:
                continue

            # Parse date — format in CSV is M/D/YYYY
            try:
                date = datetime.strptime(date_str, "%m/%d/%Y").date()
            except ValueError:
                # If date can't be parsed, skip the row
                print(f"Warning: could not parse date '{date_str}', skipping row.")
                continue

            meetings.append(Meeting(
                date=date,
                family=family,
                address=address,
                contact=contact,
            ))

    return meetings