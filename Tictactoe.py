#There will be 9 entries in the tic tac toe game initially they are blank
# We have used dictionary datatype to store the values 
d = {1:' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
#function for displaying a row in grid
def display_row(d,row_number):
    print("     |     |     ")
    print("  ",d[1 + 3*(row_number-1)],"  ","|  ",d[2+3*(row_number-1)],"  ","|  ",d[3+3*(row_number-1)],"  ",sep ='')
    print("     |     |     ")
# display_row(d,1)
#function for printing the horizontal sepration between two rows
def display_horizonal_line(n):
    for i in range(n):
        print("=",end ='')
    print(" ")
# display_horizonal_line(17)
#function for printing the tic tac toe grid print row three time and line 2 times
def display_board(d):
    for i in range(1,4):
        display_row(d,i)
        if i < 3:
            display_horizonal_line(17)
# display_board(d)
#this function takes the input
#First it asks the name of first player
#Then it asks what symbol 1st player will choose
#Then it asks for name of second player and gives second player another symbol
def player_name():   
    user_1 = input("Hi! Please enter name of first player:")  #stores the name of first user
    print("Hi" , user_1)
    user_1_char = input("Please choose your character x or o:") #stores the symbol of first user
    while(user_1_char != 'x' and user_1_char != 'o' ):
        print("Looks like you have not entered from x and o")
        user_1_char = input("Please choose your character x or o:")
    user_2 = input("Hi! Please enter name of second player:") #stores the name of second user
    if user_1_char == 'x': # condition for choosing symbol of second user.
        user_2_char = 'o'
    else:
        user_2_char = 'x'
    print(user_1,"choosed",user_1_char)
    print(user_2,"choosed",user_2_char)
    return((user_1 , user_1_char) , (user_2 , user_2_char))
#checks whether all positions in a particular row are same
#if they are same it returns true else it return false
def row_check(d,char,i):
    if d[1 + i*3] == char and d[2+i*3] == char and d[3+i*3] == char:
        return True
    else:
        return False
#checks whether all positions in a particular column are same
#if they are same it returns true else it return false
def column_check(d,char,i):
    if d[i+1] == char and d[i+4] == char and d[i+7] == char:
        return True
    else:
        return False
#checks whether all positions in a particular diagonal are same
#if they are same it returns true else it return false
def diag1_check(d,char):
    if d[1] == char and d[5] == char and d[9] == char:
        return True
    else:
        return False
#checks whether all positions in a particular diagonal are same
#if they are same it returns true else it return false
def diag2_check(d,char):
    if d[3] == char and d[5] == char and d[7] == char:
        return True
    else:
        return False
#This function returns whether a player wins or not after his move
#This function calls the above four function if any of the above function return true it will return true
def won(d,char):
    flag = 0                                            # initialize flag with zero
    for i in range(3):
        if row_check(d,char,i) == True:
            flag = 1                                    # if any condition is satisfied it return true
        if column_check(d,char,i) == True:
            flag = 1
    if diag1_check(d,char) == True or diag2_check(d,char) == True:
        flag = 1
    if flag == 1:
        return True
    else:
        return False
#check whether the matriz is completey filled or not
def complete(d):                                     
    flag = 1
    for i in range(1,10):
        if d[i] == ' ':
            flag = 0
    if flag == 0:
        return False
    else:
        return True
(user_1 , user_1_char) , (user_2 , user_2_char)= player_name()
#How number are connected to grid
ref = {1:'1', 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
print("Following are number relation to grid cells")
display_board(ref)
#first chance is by deafult assigned to player 1
player = 1
# reinitializing the whole grid
d = {1:' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
# print("\n")
# display_board(d)
while(True):
    if player == 1:   # Condition for which player to move
        print(user_1 , "Please select a cell from 1,2...9 where you want to put " , user_1_char)
        place = input()
        ls = ['1','2','3','4','5','6','7','8','9']    # Input number must be one to them
        flag1 = 1 
        flag2 = 1
        while(flag1 == 1 or flag2 == 1):
            flag1 = 1 
            flag2 = 1
            if place not in ls:    # Condition for place to in above list
                print("You have choose not choose form 1 to 9 . Please choosen from 1 - 9")
                place = input("Try again")
                continue
            else:
                flag1 = 0
            place = int(place)
            if d[place] != ' ':   # Condition for than place to be unoccupied
                print("This place is already occupied")
                place = input("Try again")
                continue
            else:
                flag2 = 0
        d[place] = user_1_char
        display_board(d)
        if won(d,user_1_char) == True:
            print("Congrats!",user_1,"you won")
            break
        player = 2                   #change the player
    else:
        print(user_2 , "Please select a cell from 1,2...9 where you want to put " , user_2_char)
        place = input()
        ls = ['1','2','3','4','5','6','7','8','9']
        flag1 = 1 
        flag2 = 1
        while(flag1 == 1 or flag2 == 1):
            flag1 = 1 
            flag2 = 1
            if place not in ls:
                print("You have choose not choose form 1 to 9 . Please choosen from 1 - 9")
                place = input("Try again")
                continue
            else:
                flag1 = 0
            place = int(place)
            if d[place] != ' ':
                print("This place is already occupied")
                place = input("Try again")
                continue
            else:
                flag2 = 0;     
        d[place] = user_2_char
        display_board(d)
        if won(d,user_2_char) == True:
            print("Congrats!",user_2,"you won")
            break
        player = 1
    if complete(d) == True:
        print("Match Draw!!!!")
        break
 
