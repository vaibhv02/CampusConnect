import streamlit as st
from app.auth import signup, signin, reset_password

def show_signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        if signup(username, password):
            st.success("User created successfully!")
        else:
            st.error("Username already exists.")

def show_signin():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        if signin(username, password):
            st.success("Signed in successfully!")
            # Redirect to the main app or set session state
            st.session_state['user'] = username
            st.experimental_rerun()  # Refresh to show main app
        else:
            st.error("Invalid username or password.")

def show_reset_password():
    st.title("Reset Password")
    username = st.text_input("Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Reset Password"):
        if reset_password(username, new_password):
            st.success("Password reset successfully!")
        else:
            st.error("Username not found.") 