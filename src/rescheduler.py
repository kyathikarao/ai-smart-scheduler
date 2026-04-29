import pandas as pd
from datetime import datetime, timedelta
from src.scheduler import schedule_tasks


def get_missed_tasks(df, current_date):
    """
    Identify tasks that missed their deadline and are not completed
    """
    df["deadline_dt"] = pd.to_datetime(df["deadline"])

    missed = df[
        (df["deadline_dt"] < pd.to_datetime(current_date)) &
        (df["status"] != "completed")
    ]

    return missed


def mark_missed_tasks(df, current_date):
    """
    Mark overdue tasks as 'missed'
    """
    df["deadline_dt"] = pd.to_datetime(df["deadline"])

    df.loc[
        (df["deadline_dt"] < pd.to_datetime(current_date)) &
        (df["status"] != "completed"),
        "status"
    ] = "missed"

    return df


def reschedule_tasks(df, current_date):
    """
    Adaptive rescheduling:
    - Take pending + missed tasks
    - Re-run scheduler on them
    """

    # Step 1: mark missed tasks
    df = mark_missed_tasks(df, current_date)

    # Step 2: filter tasks that need rescheduling
    remaining_tasks = df[df["status"] != "completed"].copy()

    if remaining_tasks.empty:
        return []

    # Step 3: reuse scheduler logic
    new_schedule = schedule_tasks(remaining_tasks)

    return new_schedule