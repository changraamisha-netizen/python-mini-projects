questions=[]
def menu():
    print("====QUIZ MANAGEMENT SYSTEM====")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Take Quiz")
    print("4. Exit")

def add_question():
    que=input("Enter Question:")
    optA=input("Enter Option A:")
    optB=input("Enter Option B:")
    optC=input("Enter Option C:")
    optD=input("Enter Option D:")
    correct=input("Enter Correct Option (A/B/C/D):")
    info={"Question":que, "A":optA, "B":optB, "C":optC, "D":optD, "answer":correct}
    questions.append(info)
    print("Question Added Successfully!")

def view_question():
    print("-----QUESTIONS-----")
    if len(questions)==0:
        print("NO DATA FOUND")
    else:
        for i, q in enumerate(questions,1):
            print("Question",i,":" ,q["Question"])
            print("A",q["A"])
            print("B",q["B"])
            print("C",q["C"])
            print("D",q["D"])

def take_quiz():
    print("-----QUIZ-----")
    score=0
    if len(questions)==0:
        print("NO DATA")
    else:
        for i, q in enumerate(questions,1):
            print("Question",i,":",q["Question"])
            print("A",q["A"])
            print("B",q["B"])
            print("C",q["C"])
            print("D",q["D"])
            answer=input("Enter your answer's option:").upper()
            if answer==q["answer"]:
                score+=1
            else:
                print("Your answer is incorrect and correct answer is:", q["answer"])
        print("Quiz Completed!")
        print("Final score is:", score,"/",len(questions))
while True:
    menu()
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_question()
    elif choice==2:
        view_question()
    elif choice==3:
        take_quiz()
    elif choice==4:
        print("EXITING PROGRAM...")
        break
    else:
        print("PLEASE ENTER A VALID CHOICE")

        


        
