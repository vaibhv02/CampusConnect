import streamlit as st
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Path to the user data file
USER_DATA_FILE = 'data/users.json'

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Load user data
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save user data
def save_users(users):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f)

# Sign up function
def signup(username, password):
    users = load_users()
    if username in users:
        return False  # User already exists
    users[username] = generate_password_hash(password)
    save_users(users)
    return True

# Sign in function
def signin(username, password):
    users = load_users()
    if username in users and check_password_hash(users[username], password):
        return True  # Successful sign-in
    return False  # Failed sign-in

# Reset password function
def reset_password(username, new_password):
    users = load_users()
    if username in users:
        users[username] = generate_password_hash(new_password)
        save_users(users)
        return True
    return False 