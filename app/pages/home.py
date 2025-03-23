import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta

def show():
    st.title("Welcome to Campus Connect")
    
    # User welcome section with customized greeting based on time of day
    current_hour = datetime.now().hour
    greeting = "Good morning" if 5 <= current_hour < 12 else "Good afternoon" if 12 <= current_hour < 18 else "Good evening"
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"### {greeting}, Student!")
        st.markdown("Your personalized academic hub is ready to help you succeed.")
    
    with col2:
        # Placeholder for profile picture or avatar
        st.image("https://via.placeholder.com/150", width=100)
    
    # Dashboard overview 
    st.markdown("## Your Dashboard")
    
    # Quick stats in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Tasks Due Today", value="3")
    
    with col2:
        st.metric(label="Upcoming Tests", value="2")
    
    with col3:
        st.metric(label="Study Streak", value="5 days")
    
    with col4:
        st.metric(label="Points", value="250")
    
    # Upcoming deadlines
    st.markdown("### Upcoming Deadlines")
    
    # Sample data - in a real app, this would come from a database
    deadlines = pd.DataFrame({
        'Assignment': ['Math Problem Set', 'History Essay', 'Physics Lab Report', 'Programming Project'],
        'Course': ['MATH 101', 'HIST 205', 'PHYS 120', 'CS 150'],
        'Due Date': ['2023-09-25', '2023-09-28', '2023-10-01', '2023-10-10'],
        'Status': ['In Progress', 'Not Started', 'In Progress', 'Not Started']
    })
    
    deadlines['Due Date'] = pd.to_datetime(deadlines['Due Date'])
    deadlines['Days Left'] = (deadlines['Due Date'] - pd.Timestamp.now()).dt.days
    
    # Apply conditional styling
    def highlight_urgent(val):
        if val <= 3:
            return 'background-color: #4a4a4a; color: white; font-weight: bold'
        elif val <= 7:
            return 'background-color: #636363; color: white'
        else:
            return ''
    
    st.dataframe(
        deadlines.style.applymap(highlight_urgent, subset=['Days Left']),
        use_container_width=True
    )
    
    # Daily study recommendation
    st.markdown("### Today's Study Recommendation")
    
    with st.container():
        st.markdown("""
        Based on your upcoming deadlines and past study patterns, we recommend:
        
        * **MATH 101**: Review calculus concepts (2 hours)
        * **HIST 205**: Begin research for your essay (1 hour)
        * **PHYS 120**: Complete practice problems 1-10 (1.5 hours)
        """)
        
        if st.button("Generate Detailed Study Plan"):
            with st.spinner("Creating your personalized study plan..."):
                time.sleep(2)  # Simulate processing
                st.success("Your detailed study plan has been created!")
                st.markdown("View it in the **Study Planner** tab.")
    
    # Recent campus activity
    st.markdown("### Campus Highlights")
    
    with st.expander("Recent Events You Might Like"):
        st.markdown("""
        * 🎭 **Drama Club Auditions** - Tomorrow, 5 PM at Student Center
        * 🧠 **AI & Machine Learning Workshop** - Sep 27, 2 PM at CS Building
        * 🏀 **Basketball Tournament** - This weekend at the Sports Complex
        """)
    
    # Tips and motivation
    st.markdown("### Daily Tip")
    st.info("💡 **Study Tip**: The Pomodoro Technique involves studying for 25 minutes, then taking a 5-minute break. Try it today to boost productivity!") 