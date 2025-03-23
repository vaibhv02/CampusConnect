import hashlib
import json
import os
import secrets
import string
from datetime import datetime, timedelta

# File to store user data
USER_DB_FILE = "data/users.json"

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = pwdhash.hex()
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64].encode('ascii')
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt, 100000)
    pwdhash = pwdhash.hex()
    return pwdhash == stored_password

def load_users():
    """Load users from the database file"""
    try:
        os.makedirs(os.path.dirname(USER_DB_FILE), exist_ok=True)
        with open(USER_DB_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is corrupted, return empty user dictionary
        return {"users": [], "reset_tokens": {}}

def save_users(users_data):
    """Save users to the database file"""
    os.makedirs(os.path.dirname(USER_DB_FILE), exist_ok=True)
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users_data, f, indent=2)

def user_exists(email):
    """Check if a user with the given email exists"""
    users_data = load_users()
    return any(user["email"].lower() == email.lower() for user in users_data["users"])

def get_user(email):
    """Get a user by email"""
    users_data = load_users()
    for user in users_data["users"]:
        if user["email"].lower() == email.lower():
            return user
    return None

def register_user(full_name, email, password):
    """Register a new user"""
    users_data = load_users()
    
    # Check if user already exists
    if user_exists(email):
        return False, "A user with this email already exists."
    
    # Create new user
    new_user = {
        "full_name": full_name,
        "email": email.lower(),
        "password": hash_password(password),
        "created_at": datetime.now().isoformat(),
    }
    
    users_data["users"].append(new_user)
    save_users(users_data)
    return True, "Registration successful! Please log in."

def authenticate_user(email, password):
    """Authenticate a user"""
    user = get_user(email)
    if not user:
        return False, "User not found."
    
    if verify_password(user["password"], password):
        return True, user
    else:
        return False, "Incorrect password."

def generate_reset_token(email):
    """Generate a password reset token"""
    if not user_exists(email):
        return False, "User not found."
    
    # Generate a secure token
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(32))
    
    # Store the token with expiration
    users_data = load_users()
    users_data["reset_tokens"][token] = {
        "email": email.lower(),
        "expires_at": (datetime.now() + timedelta(hours=1)).isoformat()
    }
    save_users(users_data)
    
    return True, token

def verify_reset_token(token):
    """Verify if a reset token is valid"""
    users_data = load_users()
    token_data = users_data["reset_tokens"].get(token)
    
    if not token_data:
        return False, "Invalid or expired token."
    
    # Check if token has expired
    expires_at = datetime.fromisoformat(token_data["expires_at"])
    if datetime.now() > expires_at:
        # Remove expired token
        del users_data["reset_tokens"][token]
        save_users(users_data)
        return False, "Token has expired."
    
    return True, token_data["email"]

def reset_password(token, new_password):
    """Reset a user's password using a valid token"""
    valid, email = verify_reset_token(token)
    if not valid:
        return False, email  # Email contains error message in this case
    
    users_data = load_users()
    
    # Update the user's password
    for user in users_data["users"]:
        if user["email"].lower() == email.lower():
            user["password"] = hash_password(new_password)
            # Remove the used token
            del users_data["reset_tokens"][token]
            save_users(users_data)
            return True, "Password has been reset successfully."
    
    return False, "User not found." 