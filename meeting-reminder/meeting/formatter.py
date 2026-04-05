# meeting/formatter.py

from meeting.models import Meeting

def format_reminder(meeting: Meeting) -> str:
    """
    Takes a Meeting object and returns a WhatsApp reminder message string.
    """
    message = (
        f"Saints, the meeting this Saturday will be at {meeting.family}'s home:\n"
        f"{meeting.address}\n"
        f"At 5:30pm as usual.\n"
        f"Please remember to check the online schedule we have as well."
    )
    return message