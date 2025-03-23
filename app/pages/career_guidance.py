import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

def show():
    st.title("Career Guidance")
    
    # Career assessment section
    st.header("Career Assessment")
    
    with st.expander("Take Career Assessment"):
        st.markdown("""
        Answer these questions to get personalized career recommendations based on your interests,
        skills, and academic background.
        """)
        
        # Sample assessment questions
        questions = [
            "What are your primary interests?",
            "What are your strongest skills?",
            "What type of work environment do you prefer?",
            "What are your salary expectations?",
            "What industries interest you the most?"
        ]
        
        answers = {}
        for q in questions:
            answers[q] = st.text_area(q)
        
        if st.button("Submit Assessment"):
            with st.spinner("Analyzing your responses..."):
                time.sleep(2)
                st.success("Assessment completed! View your personalized recommendations below.")
    
    # Career recommendations
    st.header("Your Career Recommendations")
    
    # Sample career paths
    career_paths = [
        {
            "Title": "Software Engineer",
            "Match": 95,
            "Description": "Develop software applications and systems",
            "Required Skills": ["Programming", "Problem Solving", "Team Work"],
            "Average Salary": "$85,000",
            "Growth Potential": "High"
        },
        {
            "Title": "Data Scientist",
            "Match": 90,
            "Description": "Analyze complex data sets to help organizations make better decisions",
            "Required Skills": ["Statistics", "Python", "Machine Learning"],
            "Average Salary": "$92,000",
            "Growth Potential": "Very High"
        },
        {
            "Title": "Business Analyst",
            "Match": 85,
            "Description": "Bridge the gap between IT and business objectives",
            "Required Skills": ["Analysis", "Communication", "Project Management"],
            "Average Salary": "$75,000",
            "Growth Potential": "Medium"
        }
    ]
    
    for career in career_paths:
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader(career["Title"])
                st.markdown(f"**Description:** {career['Description']}")
                st.markdown("**Required Skills:**")
                for skill in career["Required Skills"]:
                    st.markdown(f"- {skill}")
            
            with col2:
                st.metric("Match Score", f"{career['Match']}%")
                st.metric("Avg. Salary", career["Average Salary"])
                st.metric("Growth", career["Growth Potential"])
    
    # Internship opportunities
    st.header("Recommended Internships")
    
    internships = [
        {
            "Company": "Tech Corp",
            "Position": "Software Engineering Intern",
            "Location": "San Francisco, CA",
            "Duration": "Summer 2024",
            "Requirements": ["Python", "JavaScript", "Git"],
            "Application Deadline": "2024-02-01"
        },
        {
            "Company": "Data Solutions Inc",
            "Position": "Data Science Intern",
            "Location": "Remote",
            "Duration": "Summer 2024",
            "Requirements": ["Python", "SQL", "Machine Learning"],
            "Application Deadline": "2024-01-15"
        }
    ]
    
    for internship in internships:
        with st.expander(f"{internship['Company']} - {internship['Position']}"):
            st.markdown(f"**Location:** {internship['Location']}")
            st.markdown(f"**Duration:** {internship['Duration']}")
            st.markdown(f"**Application Deadline:** {internship['Application Deadline']}")
            st.markdown("**Requirements:**")
            for req in internship["Requirements"]:
                st.markdown(f"- {req}")
            
            if st.button("Apply Now", key=f"apply_{internship['Company']}"):
                st.success("Application submitted successfully!")
    
    # Resume builder
    st.header("Resume Builder")
    
    with st.form("resume_form"):
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
        
        with col2:
            location = st.text_input("Location")
            linkedin = st.text_input("LinkedIn Profile")
            portfolio = st.text_input("Portfolio Website")
        
        st.subheader("Education")
        education = st.text_area("Education History")
        
        st.subheader("Experience")
        experience = st.text_area("Work Experience")
        
        st.subheader("Skills")
        skills = st.text_area("Skills (comma-separated)")
        
        submitted = st.form_submit_button("Generate Resume")
        
        if submitted:
            st.success("Resume generated successfully!")
    
    # Career resources
    st.header("Career Resources")
    
    resources = [
        {
            "Title": "Interview Preparation Guide",
            "Type": "PDF",
            "Size": "2.5 MB",
            "Description": "Comprehensive guide for technical and behavioral interviews"
        },
        {
            "Title": "Resume Templates",
            "Type": "ZIP",
            "Size": "1.8 MB",
            "Description": "Professional resume templates for different industries"
        },
        {
            "Title": "Career Development Webinar",
            "Type": "Video",
            "Size": "45 min",
            "Description": "Learn about career planning and professional development"
        }
    ]
    
    for resource in resources:
        with st.expander(resource["Title"]):
            st.markdown(f"**Type:** {resource['Type']}")
            st.markdown(f"**Size:** {resource['Size']}")
            st.markdown(f"**Description:** {resource['Description']}")
            if st.button("Download", key=f"download_{resource['Title']}"):
                st.success("Download started!")
    
    # Career trends
    st.header("Industry Trends")
    
    # Sample trend data
    trends_data = {
        "Industry": ["Technology", "Healthcare", "Finance", "Education", "Manufacturing"],
        "Growth Rate": [15, 8, 5, 3, 2],
        "Job Openings": [5000, 3000, 2000, 1500, 1000]
    }
    
    trends_df = pd.DataFrame(trends_data)
    
    # Growth rate chart
    fig = px.bar(trends_df, x="Industry", y="Growth Rate",
                 title="Industry Growth Rates (%)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Job openings chart
    fig2 = px.bar(trends_df, x="Industry", y="Job Openings",
                  title="Current Job Openings")
    st.plotly_chart(fig2, use_container_width=True) 