# meeting/models.py

from dataclasses import dataclass

@dataclass
class Meeting:
    date: str        # Ex "4/4/2026"
    family: str      # Ex "Lou, Liwen, Henry"
    address: str     # Ex "6035 clubhouse Ln\nMukilteo, 98275"
    contact: str     # Ex "555-1234"

    def is_canceled(self) -> bool:
        """Return True if the meeting is canceled or has no data"""
        if not self.family:
            return True
        return "canceled" in self.family.lower()