# books={}
# def menu():
#     print("----LIBRARY MANAGEMENT SYSTEM----")
#     print("1.Add Book")
#     print("2.Remove Book")
#     print("3.Search Book")
#     print("4.Issue Book")
#     print("5.Return Book")
#     print("6.Display All Books")
#     print("7.Exit")

# def add_book():
#     id=input("enter book ID:")
#     title=input("Enter book title:")
#     if id in books:
#         print("Book ID already exists!")
#     else:
#         books[id]={"Title":title,"Status":"Available"}
#         print("BOOK ADDED SUCCESSFULLY!")
    
# def remove_book():
#     id=input("Enter a book id to remove:")
#     if id in books:
#         del books[id]
#         print("BOOK REMOVED!")
#     else:
#         print("BOOK ID NOT FOUND")
    
# def search_book():
#     id=input("Enter book id to search:")
#     if id in books:
#         print("BOOK FOUND!","\nTitle:", books[id]["Title"], "\nStatus:", books[id]["Status"])
#     else:
#         print("BOOK NOT FOUND!")

# def issue_book():
#     id=input("Enter book id to issue:")
#     if id in books and books[id]["Status"]=="Available":
#         books[id]["Status"]="Issued"
#         print("BOOK ISSUED SUCCESSFULLY!")
#     elif id in books and books[id]["Status"]=="Issued":
#         print("BOOK IS ALREADY ISSUED!")
#     else:
#         print("BOOK NOT FOUND!")

# def return_book():
#     id=input("Enter book id to return:")
#     if id in books and books[id]["Status"]=="Issued":
#          books[id]["Status"]="Available"
#          print("BOOK RETURNED SUCCESSFULLY!")
#     elif id in books and books[id]["Status"]=="Available":
#         print("THIS BOOK WAS NOT ISSUED!")
#     else:
#         print("BOOK NOT FOUND!")

# def display_book():
#     if len(books)==0:
#         print("Library is empty")
#     else:
#         print("Library Books:")
#         for id, book in books.items():
#             print("ID:",id,"|","Title:", books[id]["Title"],"|","Status:", books[id]["Status"])

# while True:
#     menu()
#     n=int(input("Enter your choice:"))
#     if n==1:
#         add_book()
#     elif n==2:
#         remove_book()
#     elif n==3:
#         search_book()
#     elif n==4:
#         issue_book()
#     elif n==5: 
#         return_book()
#     elif n==6:
#         display_book()
#     elif n==7:
#         print("EXITING LIBRARY SYSTEM....THANKYOU")
#         break
#     else:
#         print("INVALID CHOICE")

