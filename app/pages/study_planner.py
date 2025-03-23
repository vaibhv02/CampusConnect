import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

def show():
    st.title("Study Planner")
    
    # Tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Calendar", "Tasks", "Analytics"])
    
    # Calendar Tab
    with tab1:
        st.header("Your Study Calendar")
        
        # Date picker for calendar navigation
        selected_date = st.date_input("Select Date", datetime.now())
        
        # Generate sample week schedule
        start_of_week = selected_date - timedelta(days=selected_date.weekday())
        days = [(start_of_week + timedelta(days=i)).strftime('%A, %b %d') for i in range(7)]
        
        # Sample schedule data
        schedule_data = []
        subjects = ["MATH 101", "HIST 205", "PHYS 120", "CS 150", "ENG 110"]
        hours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        
        for day in range(7):
            for _ in range(3):  # 3 random events per day
                if day < 5:  # Weekdays have more classes
                    hour = hours[day % len(hours)]
                    schedule_data.append({
                        "Day": days[day],
                        "Start Time": f"{hour}:00",
                        "End Time": f"{hour+1}:00",
                        "Subject": subjects[day % len(subjects)],
                        "Type": "Class" if day < 5 and hour < 17 else "Study Session"
                    })
        
        schedule_df = pd.DataFrame(schedule_data)
        
        # Custom CSS for day styling
        st.markdown("""
        <style>
        div.stExpander {
            background-color: #e9ecef;
            border-radius: 5px;
            margin: 5px 0;
            transition: background-color 0.2s ease;
        }
        div.stExpander:hover {
            background-color: #c2c9d1;
        }
        div.stExpander button {
            color: #333333 !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Display weekly calendar
        st.subheader("Weekly Schedule")
        for day in days:
            with st.expander(day):
                day_schedule = schedule_df[schedule_df["Day"] == day]
                if not day_schedule.empty:
                    for _, event in day_schedule.iterrows():
                        if event["Type"] == "Class":
                            st.markdown(f"**{event['Start Time']} - {event['End Time']}**: {event['Subject']} ({event['Type']})")
                        else:
                            st.markdown(f"**{event['Start Time']} - {event['End Time']}**: {event['Subject']} ({event['Type']})")
                else:
                    st.write("No events scheduled")
        
        # Add new study session
        st.subheader("Add Study Session")
        
        col1, col2 = st.columns(2)
        with col1:
            study_date = st.date_input("Date", datetime.now())
            start_time = st.time_input("Start Time", datetime.now().replace(hour=14, minute=0))
            duration = st.number_input("Duration (hours)", min_value=0.5, max_value=5.0, value=1.0, step=0.5)
        
        with col2:
            subject = st.selectbox("Subject", subjects)
            location = st.text_input("Location", "Library")
            reminder = st.checkbox("Set Reminder", value=True)
        
        if st.button("Add to Calendar"):
            st.success(f"Added {subject} study session on {study_date} at {start_time}")
    
    # Tasks Tab
    with tab2:
        st.header("Task Management")
        
        # Task categories
        task_category = st.selectbox("Filter by category", 
                                  ["All Tasks", "Assignments", "Reading", "Projects", "Exams"])
        
        # Sample task data
        tasks = [
            {"Task": "Math Problem Set", "Due": "2023-09-25", "Subject": "MATH 101", "Priority": "High", "Status": "In Progress", "Category": "Assignments"},
            {"Task": "History Essay Research", "Due": "2023-09-22", "Subject": "HIST 205", "Priority": "Medium", "Status": "Not Started", "Category": "Assignments"},
            {"Task": "Read Physics Chapter 3", "Due": "2023-09-21", "Subject": "PHYS 120", "Priority": "Medium", "Status": "Not Started", "Category": "Reading"},
            {"Task": "Programming Project", "Due": "2023-10-10", "Subject": "CS 150", "Priority": "High", "Status": "Not Started", "Category": "Projects"},
            {"Task": "Midterm Exam Prep", "Due": "2023-10-05", "Subject": "MATH 101", "Priority": "High", "Status": "Not Started", "Category": "Exams"}
        ]
        
        tasks_df = pd.DataFrame(tasks)
        
        # Filter based on selection
        if task_category != "All Tasks":
            filtered_tasks = tasks_df[tasks_df["Category"] == task_category]
        else:
            filtered_tasks = tasks_df
        
        # Display tasks with checkbox to mark as complete
        st.subheader("Your Tasks")
        for i, task in filtered_tasks.iterrows():
            col1, col2, col3 = st.columns([0.1, 3, 1])
            with col1:
                completed = st.checkbox("", key=f"task_{i}")
            with col2:
                task_name = task["Task"]
                if completed:
                    task_name = f"~~{task_name}~~"  # Strikethrough for completed tasks
                st.markdown(f"{task_name} ({task['Subject']}) - Due: {task['Due']}")
            with col3:
                priority_color = "red" if task["Priority"] == "High" else "orange" if task["Priority"] == "Medium" else "green"
                st.markdown(f"<span style='color:{priority_color};'>{task['Priority']}</span>", unsafe_allow_html=True)
        
        # Add new task
        st.subheader("Add New Task")
        
        col1, col2 = st.columns(2)
        with col1:
            new_task = st.text_input("Task Description")
            due_date = st.date_input("Due Date", datetime.now() + timedelta(days=7))
        
        with col2:
            subject = st.selectbox("Subject", subjects, key="task_subject")
            priority = st.select_slider("Priority", options=["Low", "Medium", "High"], value="Medium")
            category = st.selectbox("Category", ["Assignments", "Reading", "Projects", "Exams"])
        
        if st.button("Add Task"):
            st.success(f"Added task: {new_task}")
    
    # Analytics Tab
    with tab3:
        st.header("Study Analytics")
        
        # Sample study time data
        study_data = {
            "Subject": ["MATH 101", "HIST 205", "PHYS 120", "CS 150", "ENG 110"],
            "Hours": [12, 8, 10, 15, 6]
        }
        
        study_df = pd.DataFrame(study_data)
        
        # Bar chart of study time by subject
        st.subheader("Study Time by Subject (Last 30 Days)")
        fig = px.bar(study_df, x="Subject", y="Hours", color="Subject",
                    title="Hours Studied per Subject")
        st.plotly_chart(fig, use_container_width=True)
        
        # Study time trends
        st.subheader("Study Time Trends")
        
        # Generate sample daily study data for the past 2 weeks
        dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(14, 0, -1)]
        daily_hours = [round(2 + i*0.2 + (i%3), 1) for i in range(14)]  # Generates sample hours with some variation
        
        daily_study = pd.DataFrame({
            "Date": dates,
            "Hours": daily_hours
        })
        
        # Line chart of daily study time
        fig2 = px.line(daily_study, x="Date", y="Hours", markers=True,
                      title="Daily Study Hours (Last 2 Weeks)")
        st.plotly_chart(fig2, use_container_width=True)
        
        # Study insights
        st.subheader("Study Insights")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Average Daily Study Time", "2.8 hours", "0.5 hours")
            st.metric("Most Studied Subject", "CS 150 (15h)", "3 hours")
        
        with col2:
            st.metric("Study Streak", "5 days", "2 days")
            st.metric("Productivity Score", "82%", "5%")
        
        st.info("💡 **Insight**: You study most effectively between 2-4 PM. Consider scheduling more sessions during this time.") 