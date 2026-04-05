# meeting/selector.py

from datetime import date, timedelta
from meeting.models import Meeting

def find_upcoming_meeting(meetings: list[Meeting], days_ahead: int = 2) -> Meeting | None:
    """
    Looks through the meeting list and returns the meeting
    that falls on (today + days_ahead).
    Returns None if no meeting is found, or if it is canceled.
    """
    target_date = date.today() + timedelta(days=days_ahead)

    for meeting in meetings:
        if meeting.date == target_date:
            if meeting.is_canceled():
                return None  # meeting exists but is canceled
            return meeting   # found a real meeting!

    return None  # no row matched the target date at all