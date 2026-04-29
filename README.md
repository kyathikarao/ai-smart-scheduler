# 🧠 AI Smart Scheduler & Adaptive To-Do System

An intelligent task scheduling and productivity system built using Python and Streamlit.  
It automatically schedules tasks, adapts to missed deadlines, and provides productivity insights.

---

## 🚀 Features

- ➕ Add and manage tasks with priority, deadline, and duration
- 🧠 Smart scheduling based on priority + deadline
- 🔁 Adaptive rescheduling for missed tasks
- 📊 Productivity insights dashboard
- 📅 Dynamic time-slot generation
- 💾 Persistent storage using CSV
- 🎨 Clean Streamlit-based UI

---

## 🏗️ System Architecture

- **Frontend:** Streamlit UI
- **Backend Logic:** Python modules (scheduler, rescheduler)
- **Storage:** CSV-based lightweight database
- **Core Engine:** Rule-based scheduling algorithm

---

## ⚙️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy

---

## 🧠 Key Concepts Used

- Greedy scheduling algorithm
- Priority-based task sorting
- Deadline-aware planning
- State management (pending / completed / missed)
- Dynamic rescheduling logic

---

## 📁 Project Structure


ai-smart-scheduler/
│── app.py
│── requirements.txt
│── README.md
│
├── data/
│ └── tasks.csv
│
├── src/
│ ├── data_handler.py
│ ├── scheduler.py
│ ├── rescheduler.py
│
└── utils/


---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
📊 Future Improvements
AI-based time estimation
Google Calendar integration
NLP task input ("remind me to study tomorrow")
Machine learning workload prediction