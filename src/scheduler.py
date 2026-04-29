import pandas as pd
from datetime import datetime, timedelta


def convert_to_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


def schedule_tasks(df, start_time="09:00", end_time="21:00"):
    """
    Generates a smart schedule based on:
    - Priority
    - Deadline
    - Duration
    """

    if df.empty:
        return []

    # Convert deadline to datetime
    df["deadline_dt"] = df["deadline"].apply(convert_to_datetime)

    # Priority mapping
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    df["priority_score"] = df["priority"].map(priority_map)

    # Sort tasks:
    # 1. High priority first
    # 2. Earliest deadline first
    df = df.sort_values(
        by=["priority_score", "deadline_dt"],
        ascending=[False, True]
    )

    schedule = []

    current_time = datetime.strptime(start_time, "%H:%M")

    end_time = datetime.strptime(end_time, "%H:%M")

    for _, task in df.iterrows():

        duration_hours = float(task["duration"])

        task_end = current_time + timedelta(hours=duration_hours)

        # If task exceeds working hours → skip to next day logic (simple version)
        if task_end > end_time:
            break

        schedule.append({
            "task_name": task["task_name"],
            "start_time": current_time.strftime("%H:%M"),
            "end_time": task_end.strftime("%H:%M"),
            "duration": task["duration"],
            "priority": task["priority"],
            "deadline": task["deadline"]
        })

        current_time = task_end

    return schedule