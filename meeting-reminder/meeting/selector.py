# meeting/selector.py

from datetime import date, timedelta
from meeting.models import Meeting

def get_this_saturday() -> date:
    today = date.today()
    days_until_saturday = (5 - today.weekday()) % 7
    return today + timedelta(days=days_until_saturday)

def find_upcoming_meeting(meetings: list[Meeting]) -> Meeting | None:
    target_date = get_this_saturday()

    for meeting in meetings:
        if meeting.date == target_date:
            if meeting.is_canceled():
                return None
            return meeting

    return None