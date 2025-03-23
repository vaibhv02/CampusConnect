import streamlit as st
from app.auth import reset_password

def show():
    st.title("Reset Password")
    username = st.text_input("Username")
    new_password = st.text_input("New Password", type="password")
    
    if st.button("Reset Password"):
        if reset_password(username, new_password):
            st.success("Password reset successfully!")
        else:
            st.error("Username not found.") 