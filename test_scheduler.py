from src.rescheduler import reschedule_tasks
from src.data_handler import load_tasks

df = load_tasks()
print(reschedule_tasks(df, "2026-04-29"))