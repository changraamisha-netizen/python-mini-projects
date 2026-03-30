# STAR PATTERN FOR "AMISHA" HORIZONTALLY

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    for col in range(5):
        if (col==0 or col==4) or ((col==1 or col==3) and row==1) or (col==2 and row==2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    for col in range(5):
        if (row==0 or row==6) or col==2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    for col in range(5):
        if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    for col in range(5):
        if (col==0 or col==4) or (row==3 and col>0 and col<4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("  ", end="")

    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()