from meeting.loader import load_meetings

meetings = load_meetings("data/UWB Students - Schedule.csv")

for m in meetings[:5]:
    print(m.date, "|", m.family, "|", m.is_canceled())