import streamlit as st
import time
from datetime import datetime

def show():
    st.title("Smart Tutor")
    
    # Introduction
    st.markdown("""
    Welcome to your AI-powered study companion! Ask questions about your coursework,
    get help with problem-solving, or request explanations of complex concepts.
    """)
    
    # Subject selection
    subject = st.selectbox(
        "Select Subject",
        ["MATH 101", "HIST 205", "PHYS 120", "CS 150", "ENG 110"]
    )
    
    # Topic selection based on subject
    topics = {
        "MATH 101": ["Calculus", "Linear Algebra", "Statistics"],
        "HIST 205": ["Ancient History", "Medieval History", "Modern History"],
        "PHYS 120": ["Mechanics", "Thermodynamics", "Electromagnetism"],
        "CS 150": ["Programming", "Data Structures", "Algorithms"],
        "ENG 110": ["Grammar", "Writing", "Literature"]
    }
    
    topic = st.selectbox("Select Topic", topics[subject])
    
    # Question input
    question = st.text_area(
        "Ask your question",
        placeholder="Type your question here...",
        height=100
    )
    
    # Additional context
    with st.expander("Add Context (Optional)"):
        st.text_area(
            "Additional Information",
            placeholder="Add any relevant context, equations, or code snippets...",
            height=100
        )
    
    # Submit button
    if st.button("Get Help"):
        if not question:
            st.warning("Please enter a question first!")
        else:
            with st.spinner("Thinking..."):
                time.sleep(2)  # Simulate AI processing
                
                # Sample response based on subject and topic
                responses = {
                    "MATH 101": {
                        "Calculus": """
                        Let me help you understand this calculus concept:
                        
                        1. First, let's break down the problem
                        2. Here's the step-by-step solution
                        3. Key points to remember:
                           - Point 1
                           - Point 2
                           - Point 3
                        
                        Would you like me to explain any part in more detail?
                        """,
                        "Linear Algebra": "Linear algebra explanation...",
                        "Statistics": "Statistics explanation..."
                    },
                    "HIST 205": {
                        "Ancient History": "Ancient history explanation...",
                        "Medieval History": "Medieval history explanation...",
                        "Modern History": "Modern history explanation..."
                    }
                }
                
                # Display response
                st.markdown("### Answer")
                if subject in responses and topic in responses[subject]:
                    st.markdown(responses[subject][topic])
                else:
                    st.markdown("""
                    Here's a detailed explanation of your question:
                    
                    1. First point
                    2. Second point
                    3. Third point
                    
                    Would you like me to elaborate on any of these points?
                    """)
                
                # Follow-up options
                st.markdown("### Need More Help?")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("Explain Further"):
                        st.info("Let me break this down in more detail...")
                
                with col2:
                    if st.button("Show Examples"):
                        st.info("Here are some practical examples...")
                
                with col3:
                    if st.button("Practice Problems"):
                        st.info("Let's try some practice problems...")
    
    # Study tips section
    st.markdown("### Study Tips")
    tips = [
        "Break down complex problems into smaller parts",
        "Practice with similar examples",
        "Create flashcards for key concepts",
        "Teach the concept to someone else",
        "Review regularly to reinforce learning"
    ]
    
    for tip in tips:
        st.markdown(f"* {tip}")
    
    # Recent questions history
    st.markdown("### Recent Questions")
    recent_questions = [
        {"question": "How do I solve quadratic equations?", "subject": "MATH 101", "date": "2023-09-20"},
        {"question": "What were the main causes of World War II?", "subject": "HIST 205", "date": "2023-09-19"},
        {"question": "Can you explain Newton's laws?", "subject": "PHYS 120", "date": "2023-09-18"}
    ]
    
    for q in recent_questions:
        with st.expander(f"{q['subject']} - {q['date']}"):
            st.markdown(q["question"]) 