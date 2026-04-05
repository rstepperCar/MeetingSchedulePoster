# test_formatter.py

from meeting.models import Meeting
from meeting.formatter import format_reminder
from datetime import date

def test_formatter():
    meeting = Meeting(
        date=date(2026, 4, 11),
        family="Chok, Nancy",
        address="7416 Ne 198th Pl, Kenmore WA 98028",
        contact=""
    )

    message = format_reminder(meeting)
    print(message)

test_formatter()