import streamlit as st
import sqlite3
import time

st.set_page_config(layout="wide")
def db_connect():
    return sqlite3.connect('atm1.db')

def create_table():
    conn = db_connect()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS ACCOUNT (ACCNO INTEGER PRIMARY KEY AUTOINCREMENT,HOLDER_NAME TEXT NOT NULL, PIN TEXT,
            BALANCE INTEGER  CHECK(BALANCE>=1000), TYPE TEXT ) ''')
    conn.commit()
    conn.close()

def get_user(accno):
    if accno is None:
        return None
    conn = db_connect()
    c = conn.cursor()
    c.execute("SELECT * FROM ACCOUNT WHERE ACCNO=?", (int(accno),))
    data = c.fetchone()
    conn.close()
    return data

def get_balance(accno):
    user = get_user(accno)
    return user[3] if user else None
    
def deposit(accno, amount):
    user = get_user(accno)
    if not user:
        return "Account not found"
    new_balance = user[3] + amount 
    conn = db_connect()
    c = conn.cursor()
    c.execute("UPDATE ACCOUNT SET BALANCE=? WHERE ACCNO=?", (new_balance, accno))
    conn.commit()
    conn.close()
    return f"Deposit Successful, New Balance:{new_balance}"

def withdraw(accno, amount):
    user = get_user(accno)
    if not user:
        return "Account not found"
    current_balance = user[3]
    if amount > current_balance - 1000:
        return f"Insufficient Balance: Minimum balance of 1000 must be maintained, so firstly deposit some money."
    new_balance = current_balance - amount
    conn = db_connect()
    c = conn.cursor()
    c.execute("UPDATE ACCOUNT SET BALANCE=? WHERE ACCNO=?", (new_balance, accno))
    conn.commit()
    conn.close()
    return f"Withdrawal Successful, New Balance: {new_balance}"

def change_pin(accno, old_pin, new_pin, confirm):
    user = get_user(accno)
    if not user:
        return "Account not found"
    if user[2] != old_pin:
        return "Incorrect old PIN"
    if len(new_pin) != 4 or not new_pin.isdigit():
        return "PIN must be 4 digits"
    if old_pin==new_pin:
        return "Old pin and new pin are same"
    if confirm!=new_pin:
        return "New pin and confirm pin not match"
    conn = db_connect()
    c = conn.cursor()
    c.execute("UPDATE ACCOUNT SET PIN=? WHERE ACCNO=?", (new_pin, accno))
    conn.commit()
    conn.close()
    return "PIN Updated Successfully"

if "accno" not in st.session_state:
    st.session_state.accno = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"
if "sidebar_choice" not in st.session_state:
    st.session_state.sidebar_choice = "Home"

def top_bar():
    user = get_user(st.session_state.accno)
    if user:
        st.write(f"Account No: {user[0]}    |    {user[1]}")
        st.write("---")

def sidebar_menu():
    if not st.session_state.logged_in:
        return
    choice = st.sidebar.radio("ATM Menu", [ "Home", "Deposit", "Withdraw", "Check Balance", "Change PIN", "Logout"], 
                              index=["Home","Deposit","Withdraw","Check Balance","Change PIN","Logout"].index(st.session_state.sidebar_choice))

    if choice != st.session_state.sidebar_choice:
        st.session_state.sidebar_choice = choice
        if choice == "Logout":
            st.session_state.clear()
            st.rerun()
        else:
            mapping = {
                "Home": "home",
                "Deposit": "deposit",
                "Withdraw": "withdraw",
                "Check Balance": "balance",
                "Change PIN": "pin"
            }
            st.session_state.page = mapping[choice]
            st.rerun()

def signin(accno, pin):
    user = get_user(accno)
    if not user:
        st.error("Account not exist")
    elif user[2]!=pin:
        st.error("Incorrect PIN")
    elif user and user[2] == pin:
        st.session_state.accno = user[0]
        st.session_state.logged_in = True
        st.session_state.page = "home"
        st.rerun()

def login_page():
    st.title("ATM Login")
    accno = st.number_input("Account Number",step=1)
    pin = st.text_input("PIN", type="password")
    if st.button("Login"):
        signin(accno, pin)
    if st.button("Create Account"):
        st.session_state.page = "signup"
        st.rerun()

def signup_page():
    st.title("Create Account")
    name = st.text_input("Name")
    pin = st.text_input("Create PIN", type="password")
    confirm_pin = st.text_input("Confirm PIN", type="password")
    acc_type = st.selectbox("Account Type", ["Saving", "Current"])

    if st.button("Create Account"):
        if name == "":
            st.error("Name cannot be empty")
        elif pin != confirm_pin:
            st.error("PIN does not match")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be 4 digits")
        else:
            conn = db_connect()
            c = conn.cursor()
            c.execute("INSERT INTO ACCOUNT(HOLDER_NAME, PIN, BALANCE, TYPE) VALUES (?, ?, ?, ?)",
                      (name, pin, 1000, acc_type))
            conn.commit()
            accno = c.lastrowid
            conn.close()
            st.success(f"Account Created! Your Account Number: {accno}")
            time.sleep(2)
            st.session_state.page = "login"
            st.rerun()

def home_page():
    sidebar_menu()
    top_bar()
    st.title("ATM Dashboard")
    st.success("Welcome! Use the sidebar to perform actions.")

def deposit_page():
    sidebar_menu()
    top_bar()
    st.title("Deposit Money")
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Deposit"):
        msg = deposit(st.session_state.accno, amount)
        if "Successful" in msg :
            st.success(msg)
        else:
            st.error(msg)

def withdraw_page():
    sidebar_menu()
    top_bar()
    st.title("Withdraw Money")
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Withdraw"):
        msg = withdraw(st.session_state.accno, amount)
        if "Successful" in msg:
            st.success(msg)
        else:
            st.error(msg)

def balance_page():
    sidebar_menu()
    top_bar()
    st.title("Check Balance")
    bal = get_balance(st.session_state.accno)
    if bal is not None:
        st.success(f"Available Balance: Rupees {bal}")
    else:
        st.error("Account not found")

def pin_page():
    sidebar_menu()
    top_bar()
    st.title("Change PIN")
    old_pin = st.text_input("Old PIN", type="password")
    new_pin = st.text_input("New PIN", type="password")
    confirm=st.text_input("Confirm PIN", type="password")
    if st.button("Update PIN"):
        msg = change_pin(st.session_state.accno, old_pin, new_pin, confirm)
        if msg == "PIN Updated Successfully":
            st.success(msg)
        else:
            st.error(msg)
            
def main():
    create_table()
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "signup":
        signup_page()
    elif st.session_state.logged_in:
        if st.session_state.page == "home":
            home_page()
        elif st.session_state.page == "deposit":
            deposit_page()
        elif st.session_state.page == "withdraw":
            withdraw_page()
        elif st.session_state.page == "balance":
            balance_page()
        elif st.session_state.page == "pin":
            pin_page()

if __name__ == "__main__":
    main()