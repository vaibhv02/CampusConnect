import streamlit as st
from app.utils.auth import (
    register_user, 
    authenticate_user, 
    generate_reset_token, 
    verify_reset_token,
    reset_password
)

def show():
    # Add custom CSS
    st.markdown("""
    <style>
    .auth-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state for authentication
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user" not in st.session_state:
        st.session_state.user = None
    if "auth_page" not in st.session_state:
        st.session_state.auth_page = "login"
        
    # If user is already authenticated, show logout option
    if st.session_state.authenticated:
        st.write(f"Logged in as: **{st.session_state.user['full_name']}**")
        if st.button("Log Out"):
            st.session_state.authenticated = False
            st.session_state.user = None
            st.experimental_rerun()
        return
    
    # Container for auth forms
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Login", use_container_width=True, 
                   disabled=st.session_state.auth_page == "login"):
            st.session_state.auth_page = "login"
            st.experimental_rerun()
    with col2:
        if st.button("Sign Up", use_container_width=True, 
                   disabled=st.session_state.auth_page == "signup"):
            st.session_state.auth_page = "signup"
            st.experimental_rerun()
    with col3:
        if st.button("Reset", use_container_width=True, 
                   disabled=st.session_state.auth_page == "reset"):
            st.session_state.auth_page = "reset"
            st.experimental_rerun()
    
    # Display the appropriate form based on the selected page
    if st.session_state.auth_page == "login":
        login_form()
    elif st.session_state.auth_page == "signup":
        signup_form()
    elif st.session_state.auth_page == "reset":
        if "reset_token" not in st.session_state or not st.session_state.reset_token:
            reset_request_form()
        else:
            reset_password_form()
    
    st.markdown('</div>', unsafe_allow_html=True)

def login_form():
    """Display the login form"""
    st.subheader("Login")
    
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if not email or not password:
                st.error("Please fill in all fields.")
                return
                
            success, result = authenticate_user(email, password)
            if success:
                st.session_state.authenticated = True
                st.session_state.user = result
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error(result)

def signup_form():
    """Display the signup form"""
    st.subheader("Create an Account")
    
    with st.form("signup_form"):
        full_name = st.text_input("Full Name", key="signup_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm")
        
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            if not full_name or not email or not password or not confirm_password:
                st.error("Please fill in all fields.")
                return
                
            if password != confirm_password:
                st.error("Passwords do not match.")
                return
                
            if len(password) < 6:
                st.error("Password must be at least 6 characters long.")
                return
                
            success, message = register_user(full_name, email, password)
            if success:
                st.success(message)
                st.session_state.auth_page = "login"
                st.experimental_rerun()
            else:
                st.error(message)

def reset_request_form():
    """Display the password reset request form"""
    st.subheader("Reset Password")
    st.write("Enter your email to receive a password reset link.")
    
    with st.form("reset_request_form"):
        email = st.text_input("Email", key="reset_email")
        submit = st.form_submit_button("Send Reset Link")
        
        if submit:
            if not email:
                st.error("Please enter your email.")
                return
                
            success, token = generate_reset_token(email)
            if success:
                # In a real app, you would send an email with the reset link
                # For this demo, we'll just store the token in session state
                st.session_state.reset_token = token
                st.session_state.reset_email = email
                st.success("Password reset link generated. In a real application, this would be emailed to you.")
                st.experimental_rerun()
            else:
                st.error(token)  # Token contains error message in this case

def reset_password_form():
    """Display the password reset form"""
    st.subheader("Create New Password")
    st.write(f"Reset password for: {st.session_state.reset_email}")
    
    with st.form("reset_password_form"):
        new_password = st.text_input("New Password", type="password", key="new_password")
        confirm_password = st.text_input("Confirm New Password", type="password", key="confirm_new_password")
        
        submit = st.form_submit_button("Reset Password")
        cancel = st.form_submit_button("Cancel")
        
        if cancel:
            st.session_state.reset_token = None
            st.session_state.reset_email = None
            st.experimental_rerun()
            
        if submit:
            if not new_password or not confirm_password:
                st.error("Please fill in all fields.")
                return
                
            if new_password != confirm_password:
                st.error("Passwords do not match.")
                return
                
            if len(new_password) < 6:
                st.error("Password must be at least 6 characters long.")
                return
                
            success, message = reset_password(st.session_state.reset_token, new_password)
            if success:
                st.success(message)
                # Clear reset token and return to login
                st.session_state.reset_token = None
                st.session_state.reset_email = None
                st.session_state.auth_page = "login"
                st.experimental_rerun()
            else:
                st.error(message) 