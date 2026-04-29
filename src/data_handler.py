import pandas as pd
import os
from datetime import datetime

DATA_PATH = "data/tasks.csv"


def ensure_file_exists():
    """Creates CSV file if it doesn't exist"""
    if not os.path.exists(DATA_PATH):
        df = pd.DataFrame(columns=[
            "task_name",
            "deadline",
            "duration",
            "priority",
            "status"
        ])
        df.to_csv(DATA_PATH, index=False)


def load_tasks():
    """Load all tasks from CSV"""
    ensure_file_exists()
    return pd.read_csv(DATA_PATH)


def save_tasks(df):
    """Save dataframe back to CSV"""
    df.to_csv(DATA_PATH, index=False)


def add_task(task_name, deadline, duration, priority):
    """
    Add a new task to storage
    """
    df = load_tasks()

    new_task = {
        "task_name": task_name,
        "deadline": deadline,
        "duration": duration,
        "priority": priority,
        "status": "pending"
    }

    df = pd.concat([df, pd.DataFrame([new_task])], ignore_index=True)
    save_tasks(df)


def update_task_status(task_name, status):
    """
    Update status: completed / missed / pending
    """
    df = load_tasks()

    df.loc[df["task_name"] == task_name, "status"] = status

    save_tasks(df)