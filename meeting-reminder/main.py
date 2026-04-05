# main.py

from meeting.loader import load_meetings
from meeting.selector import find_upcoming_meeting
from meeting.formatter import format_reminder

def main():
    meetings = load_meetings("data/UWB Students - Schedule.csv")
    meeting = find_upcoming_meeting(meetings)

    if meeting is None:
        print("No meeting found for this Saturday.")
    else:
        message = format_reminder(meeting)
        print(message)

main()