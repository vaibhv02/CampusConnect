import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

def show():
    st.title("Campus Events")
    
    # Event categories
    categories = ["All Events", "Academic", "Social", "Sports", "Career", "Workshops"]
    selected_category = st.selectbox("Filter by Category", categories)
    
    # Sample event data
    events = [
        {
            "Title": "AI & Machine Learning Workshop",
            "Category": "Workshops",
            "Date": "2023-09-27",
            "Time": "14:00",
            "Location": "CS Building Room 101",
            "Description": "Learn about the latest developments in AI and ML",
            "Attendees": 45,
            "Max Capacity": 50,
            "Tags": ["AI", "Technology", "Workshop"]
        },
        {
            "Title": "Basketball Tournament",
            "Category": "Sports",
            "Date": "2023-09-30",
            "Time": "15:00",
            "Location": "Sports Complex",
            "Description": "Annual inter-department basketball tournament",
            "Attendees": 120,
            "Max Capacity": 200,
            "Tags": ["Sports", "Tournament", "Basketball"]
        },
        {
            "Title": "Career Fair 2023",
            "Category": "Career",
            "Date": "2023-10-05",
            "Time": "10:00",
            "Location": "Student Center",
            "Description": "Connect with top companies and explore internship opportunities",
            "Attendees": 300,
            "Max Capacity": 500,
            "Tags": ["Career", "Internship", "Networking"]
        },
        {
            "Title": "Study Group: Calculus",
            "Category": "Academic",
            "Date": "2023-09-25",
            "Time": "16:00",
            "Location": "Library Room 204",
            "Description": "Weekly study group for MATH 101 students",
            "Attendees": 15,
            "Max Capacity": 20,
            "Tags": ["Study Group", "Math", "Academic"]
        },
        {
            "Title": "Movie Night",
            "Category": "Social",
            "Date": "2023-09-28",
            "Time": "19:00",
            "Location": "Student Lounge",
            "Description": "Watch and discuss the latest blockbuster",
            "Attendees": 80,
            "Max Capacity": 100,
            "Tags": ["Social", "Entertainment", "Movie"]
        }
    ]
    
    events_df = pd.DataFrame(events)
    
    # Filter events based on category
    if selected_category != "All Events":
        events_df = events_df[events_df["Category"] == selected_category]
    
    # Display events in a grid
    for _, event in events_df.iterrows():
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader(event["Title"])
                st.markdown(f"**Date & Time:** {event['Date']} at {event['Time']}")
                st.markdown(f"**Location:** {event['Location']}")
                st.markdown(f"**Description:** {event['Description']}")
                
                # Tags
                tags_html = " ".join([f'<span style="background-color: #e1e1e1; padding: 2px 8px; border-radius: 12px; margin-right: 5px;">{tag}</span>' for tag in event["Tags"]])
                st.markdown(tags_html, unsafe_allow_html=True)
            
            with col2:
                # Attendance progress bar
                progress = event["Attendees"] / event["Max Capacity"]
                st.progress(progress)
                st.markdown(f"{event['Attendees']}/{event['Max Capacity']} attendees")
                
                if event["Attendees"] < event["Max Capacity"]:
                    if st.button("RSVP", key=f"rsvp_{event['Title']}"):
                        st.success("You've successfully RSVP'd for this event!")
                else:
                    st.warning("Event is full!")
    
    # Event analytics
    st.markdown("### Event Analytics")
    
    # Category distribution
    category_counts = events_df["Category"].value_counts()
    fig = px.pie(values=category_counts.values, names=category_counts.index,
                 title="Event Distribution by Category")
    st.plotly_chart(fig, use_container_width=True)
    
    # Upcoming events timeline
    st.markdown("### Upcoming Events Timeline")
    events_df["DateTime"] = pd.to_datetime(events_df["Date"] + " " + events_df["Time"])
    events_df = events_df.sort_values("DateTime")
    
    fig2 = px.scatter(events_df, x="DateTime", y="Title",
                     title="Upcoming Events Timeline",
                     labels={"DateTime": "Date & Time", "Title": "Event"})
    st.plotly_chart(fig2, use_container_width=True)
    
    # Event recommendations
    st.markdown("### Recommended for You")
    
    # Sample recommendations based on user interests
    recommendations = [
        {
            "Event": "Data Science Workshop",
            "Reason": "Based on your interest in technology and data analysis",
            "Match": "95%"
        },
        {
            "Event": "Study Group: Physics",
            "Reason": "Matches your current course schedule",
            "Match": "90%"
        },
        {
            "Event": "Career Fair 2023",
            "Reason": "Aligns with your career interests",
            "Match": "85%"
        }
    ]
    
    for rec in recommendations:
        with st.expander(f"{rec['Event']} ({rec['Match']} match)"):
            st.markdown(rec["Reason"])
    
    # Create new event form
    st.markdown("### Create New Event")
    
    with st.form("new_event_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            title = st.text_input("Event Title")
            category = st.selectbox("Category", categories[1:])  # Exclude "All Events"
            date = st.date_input("Date")
            time = st.time_input("Time")
        
        with col2:
            location = st.text_input("Location")
            description = st.text_area("Description")
            max_capacity = st.number_input("Maximum Capacity", min_value=1, value=50)
            tags = st.text_input("Tags (comma-separated)")
        
        submitted = st.form_submit_button("Create Event")
        
        if submitted:
            st.success("Event created successfully!") 