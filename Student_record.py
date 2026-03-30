student_record="student_records1.txt"
f=open(student_record, "x")

def menu():
    print("----STUDENT RECORD MANAGEMENT----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    roll=input("Enter roll number:")
    name=input("Enter name of student:")
    marks=input("Enter the marks of student:")
    f=open(student_record, "r")
    data=f.readlines()
    f.close()
    for line in data:
        r, n, m = line.strip().split(",")
        if r == roll:
            print("Roll number already exists. Cannot add duplicate record.")
            return
    f=open(student_record,"a")
    f.write(f"{roll},{name},{marks}\n")
    print("data added")
    f.close()

def view_student():
    f=open(student_record, "r")
    data=f.readlines()
    if len(data)==0:
        print("NO RECORD EXISTS!")
    else:
        for line in data:
            roll,name,marks=line.strip().split(",")
            print(f"Roll no:{roll}|Name:{name}|Marks:{marks}")
    f.close()

def search_student():
    n=input("Enter roll number to search:")
    f=open(student_record,"r")
    data=f.readlines()
    found = False
    for line in data:
        roll,name,marks=line.strip().split(",")
        if roll == n:
            print("Data found")
            print("Roll no.:",roll)
            print("Name:",name)
            print("Marks:",marks)
            found = True
            break
    if not found:
        print("Data not found")
    f.close()

def delete_student():
    n=input("Enter roll number to delete record:")
    f=open(student_record, "r")
    data=f.readlines()
    f=open(student_record, "w")
    found = False
    for line in data:
        roll,name,marks=line.strip().split(",")
        if roll != n:
            f.write(f"{roll},{name},{marks}\n")
        else:
            found = True
    if found:
        print("Record deleted")
    else:
        print("Record not found")
    f.close()

while True:
    menu()
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        search_student()
    elif choice==4:
        delete_student()
    elif choice==5:
        print("EXITING PROGRAM")
        break
    else:
        print("INVALID CHOICE!")
