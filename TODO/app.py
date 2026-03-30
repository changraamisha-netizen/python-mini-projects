import streamlit as st
from datetime import datetime
import sqlite3

st.set_page_config(layout="wide")

def create_table():
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS TO_DO (TASK_ID INTEGER PRIMARY KEY AUTOINCREMENT,TASK_NAME TEXT,TASK_STATUS TEXT, CREATED DATETIME)''')
    conn.commit()
    conn.close()

def add_task(task):
    current=datetime.now()
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('INSERT INTO TO_DO (TASK_NAME,TASK_STATUS,CREATED)VALUES(?,?,?)',(task,'Incomplete',current))
    conn.commit()
    conn.close()

def get_task():
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('SELECT TASK_ID,TASK_NAME,TASK_STATUS,CREATED FROM TO_DO')
    tasks=c.fetchall()
    conn.commit()
    conn.close()
    return tasks

def update_task(task_id,task_status):
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('UPDATE TO_DO SET TASK_STATUS=? WHERE TASK_ID=?',(task_status,task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn=sqlite3.connect('todo.db')
    c=conn.cursor()
    c.execute('DELETE FROM TO_DO WHERE TASK_ID=?',(task_id,))
    conn.commit()
    conn.close()

def main():
    st.title("Simple streamlit TO DO LIST")
    create_table()
    new_task=st.text_input("Enter your new task:")
    if st.button('Add Task'):
        if new_task:
            add_task(new_task)
            st.success(f"Your {new_task} has been added successfully")
        else:
            st.warning(f"Please enter a task")
    
    st.header("Tasks List")
    tasks=get_task()
    for task in tasks:
        task_id, task_name, task_status, created=task
        checkbox_id=f"complete_checkbox{task_id}"
        delete_id=f"delete_button{task_id}"
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.write(f'**Task ID:** {task_id} at {created}')
        with col2:
            st.write(f'**Task:** {task_name}')
        with col3:
            is_checked = st.checkbox('Mark as Complete',value=(task_status == 'Complete'),key=checkbox_id)
            if is_checked and task_status == 'Incomplete':
                update_task(task_id, 'Complete')
                st.rerun()
            elif not is_checked and task_status == 'Complete':
                update_task(task_id, 'Incomplete')
                st.rerun()
        with col4:
            if st.button('X', key=delete_id,type="primary"):
                delete_task(task_id)
                st.success('Task deleted!')
                st.rerun()
        st.write('----')
if __name__=='__main__':
    main()  


