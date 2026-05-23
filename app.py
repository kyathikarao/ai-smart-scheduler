import streamlit as st
import pandas as pd

from src.data_handler import add_task, load_tasks
from src.scheduler import schedule_tasks
from src.rescheduler import reschedule_tasks


st.set_page_config(page_title="AI Smart Scheduler", layout="wide")

st.title("🧠 AI Smart Scheduler & Adaptive To-Do System")


# =========================
# SIDEBAR - ADD TASK
# =========================
st.sidebar.header("➕ Add New Task")

task_name = st.sidebar.text_input("Task Name")

deadline = st.sidebar.date_input("Deadline")

duration = st.sidebar.number_input("Duration (hours)", min_value=0.5, step=0.5)

priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"])


if st.sidebar.button("Add Task"):
    if task_name:
        add_task(
            task_name,
            deadline.strftime("%Y-%m-%d"),
            duration,
            priority
        )
        st.sidebar.success("Task Added!")
    else:
        st.sidebar.error("Enter task name")


# =========================
# LOAD DATA
# =========================
df = load_tasks()


# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs([
    "📋 Schedule View",
    "📊 Insights Dashboard",
    "🔁 Adaptive Rescheduler"
])


# =========================
# TAB 1 - SCHEDULE
# =========================
with tab1:
    st.subheader("Generated Smart Schedule")

    if df.empty:
        st.info("No tasks available")

    else:
        schedule = schedule_tasks(df)

        if schedule:
            schedule_df = pd.DataFrame(schedule)
            st.table(schedule_df)

            st.markdown("### ✅ Mark Task as Completed")

            task_to_complete = st.selectbox(
                "Select task",
                df["task_name"].tolist()
            )

            if st.button("Mark Completed"):
                update_task_status(task_to_complete, "completed")
                st.success(f"{task_to_complete} marked as completed!")
                st.rerun()


# =========================
# TAB 2 - INSIGHTS
# =========================
with tab2:
    st.subheader("📊 Productivity Insights")

    if df.empty:
        st.info("No data yet")
    else:
        total = len(df)
        completed = len(df[df["status"] == "completed"])
        missed = len(df[df["status"] == "missed"])

        st.metric("Total Tasks", total)
        st.metric("Completed Tasks", completed)
        st.metric("Missed Tasks", missed)

        completion_rate = (completed / total) * 100 if total > 0 else 0

        st.write(f"### Completion Rate: {completion_rate:.2f}%")

        st.bar_chart(df["priority"].value_counts())


# =========================
# TAB 3 - RESCHEDULER
# =========================
with tab3:
    st.subheader("🔁 Adaptive Rescheduling System")

    if st.button("Run Rescheduler"):
        new_schedule = reschedule_tasks(df, "2026-04-29")

        if new_schedule:
            st.success("Schedule Updated!")
            st.table(pd.DataFrame(new_schedule))
        else:
            st.info("No pending tasks to reschedule")