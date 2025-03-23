import streamlit as st
from app.auth import signin

def show():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign In"):
        if signin(username, password):
            st.success("Signed in successfully!")
            # Redirect to the main app or set session state
            st.session_state['username'] = username
            st.experimental_rerun()  # Reload the app
        else:
            st.error("Invalid username or password.") 