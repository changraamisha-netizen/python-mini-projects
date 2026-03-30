import streamlit as st 
st.set_page_config(page_title="Calculator",layout="centered")
st.title("CALCULATOR")

if "prev" not in st.session_state:
    st.session_state.prev = ""
if "op" not in st.session_state:
    st.session_state.op = ""
if "curr" not in st.session_state:
    st.session_state.curr = ""

st.text_input("Display", value=st.session_state.prev+""+ st.session_state.op+""+ st.session_state.curr, disabled=True)

def press(num):
    st.session_state.curr = st.session_state.curr + str(num)

def operator(op):
    if st.session_state.prev == "":
        st.session_state.prev = st.session_state.curr
        st.session_state.curr = ""
    st.session_state.op = op
    
def equal():
    prev = float(st.session_state.prev)
    curr = float(st.session_state.curr)

    if st.session_state.op == "+":
        res = prev+curr
    elif st.session_state.op == "-":
        res = prev-curr
    elif st.session_state.op == "*":
        res = prev*curr
    elif st.session_state.op == "/":
        res = prev/curr
        
    st.session_state.prev = str(res)
    st.session_state.curr=""
    st.session_state.op=""

def clear():
        st.session_state.prev = ""
        st.session_state.curr=""
        st.session_state.op=""
        
col1,col2,col3,col4=st.columns(4)
with col1:
    st.button("1", on_click=press, args=(1,))
    st.button("2", on_click=press, args=(2,))
    st.button("3", on_click=press, args=(3,))
    st.button("+", on_click=operator, args=("+",))

with col2:
    st.button("4", on_click=press, args=(4,))
    st.button("5", on_click=press, args=(5,))
    st.button("6", on_click=press, args=(6,))
    st.button("-", on_click=operator, args=("-",))


with col3:
    st.button("7", on_click=press, args=(7,))
    st.button("8", on_click=press, args=(8,))
    st.button("9", on_click=press, args=(9,))
    st.button("*", on_click=operator, args=("*",))

with col4:
    st.button(".", on_click=press, args=(".",))
    st.button("0", on_click=press, args=(0,))
    st.button("C", on_click=clear)
    st.button("/", on_click=operator, args=("/",))


st.button("=", on_click=equal)