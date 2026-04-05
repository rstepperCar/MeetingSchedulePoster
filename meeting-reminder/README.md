# Meeting Reminder App

A Python command-line tool that reads the meeting schedule (CSV) and generates a WhatsApp reminder message in Roger's format.

---

## How to Run

1. Clone the repo
2. Place the schedule CSV in the `data/` folder
3. Run:
```bash
python3 main.py
```

---

## Project Structure
```
meeting-reminder/
├── data/
│   └── UWB Students - Schedule.csv
├── meeting/
│   ├── models.py       # Meeting dataclass
│   ├── loader.py       # Reads CSV → list of Meeting objects
│   ├── selector.py     # Finds upcoming meeting 2 days ahead
│   └── formatter.py    # Generates WhatsApp message string
├── main.py             # Entry point
├── test_models.py
├── test_loader.py
└── test_formatter.py
```

---

## Status

- ✅ V0 Complete — command line prototype
- ⬜ V1 — simple web app (coming soon)

