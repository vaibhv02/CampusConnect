import streamlit as st
from app.auth import signup

def show():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        if signup(username, password):
            st.success("User created successfully!")
        else:
            st.error("Username already exists.") 