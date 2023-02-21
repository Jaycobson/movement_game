
move = "ULRRULLLLURDL"
def finalMovePosition(move):
    """
    The goal of this project is to calculate the moves of an object in a grid
    up means it goes up by 1 unit
    down means it goes down by 1 unit
    right means it moves to the right by 1 unit
    left means it moves to the left by 1 unit

    """

    #length of string
    l = len(move)

    up,down,left,right = 0,0,0,0

    for i in range(l):
        if move[i] == 'U':
            up+=1
        elif move[i] == "D":
            down +=1
        elif move[i] == "L":
            left +=1
        elif move[i] == "R":
            right +=1

    print("Final Position: (", (right - left), ", ", (up - down), ")")
    
# The above code gives the final position of the object

move = input("Enter letters like UDLR, they mean up,down,left and right respectively ").upper()
finalMovePosition(move)