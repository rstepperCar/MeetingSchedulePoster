# test_models.py

from meeting.models import Meeting

m1 = Meeting("4/4/2026", "Lou, Liwen, Henry", "6035 clubhouse Ln", "417-849-3518")
print(m1.is_canceled())  # 應該印 False

m2 = Meeting("3/14/2026", "Meeting canceled", "No address", "")
print(m2.is_canceled())  # 應該印 True

m3 = Meeting("5/16/2026", "", "", "")
print(m3.is_canceled())  # 應該印 True