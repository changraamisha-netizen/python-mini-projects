import streamlit as st

if 'users' not in st.session_state:
    st.session_state.users = {}
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

def login(username, password):
    if username in st.session_state.users and st.session_state.users[username]['password'] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Logged in successfully!")
    else:
        st.error("Invalid credentials or register first")

def register(username, email, password):
    if username in st.session_state.users:
        st.error("Username already exists")
    else:
        st.session_state.users[username] = {'email': email, 'password': password}
        st.success("Registered successfully!")

def home():
    if st.session_state.logged_in:
        st.write(f"Hello, {st.session_state.username}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
    else:
        st.write("Please login first")

with st.sidebar:
    st.header("Navigation")
    select_option = st.radio("Go to", ["Login", "Register", "Home"])

if select_option== "Login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)

elif select_option== "Register":
    st.title("Registration")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password == confirm_password:
            register(username, email, password)
        else:
            st.error("Passwords do not match")

elif select_option == "Home":
    st.title("Home Page")
    home()