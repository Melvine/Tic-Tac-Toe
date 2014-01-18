def printBoard(gameMat):
    """
    prints the current game
    """
    print(gameMat[0]) #row 1
    print(gameMat[1]) #row 2
    print(gameMat[2]) #row 3

def checkWin(letter,board):
    """
    algorithm to check for the wins
    """
    #checks for horizontal wins
    count = 0
    for r in range(3):
        count = 0
        for k in range(3):
            if board[r][k] == letter:
                count = count + 1
        if count == 3:
            print(letter + " wins")
            return False
            
    #checks for vertical wins       
    count = 0
    for k in range(3):
        count = 0
        for r in range(3):
            if board[r][k] == letter:
                count = count + 1
        if count == 3:
            print(letter + " wins")
            return False
        
    #checks for skewed right diagonals
    count = 0
    r = 0
    for k in range(3):
        if board[r][k] == letter:
                count = count + 1
        if count == 3:
            print(letter + " wins")
            return False
        r = r + 1

    #checks for skewed left diagonals
    count = 0
    r = 2
    for k in range(3):
        if board[r][k] == letter:
                count = count + 1
        if count == 3:
            print(letter + " wins")
            return False
        r = r - 1
    
    #checks for a tie in the game
    count = 0
    for r in range(3):
        for k in range(3):
            if board[r][k] != '-':
                count = count + 1
        if count == 9:
            print(letter + " tie")
            return False
    return True
    
def game():
    """
    changes the board to x and o
    uses printBoard to update the users ui and checkWin to find winner
    """
    #intializes the board
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    printBoard(board)
    x = True #initialize x as True to loop the game, False when there is a winner
   
    #user inputs 
    while x:
        n = input("Please enter 'x' or 'o':")
        while n.strip() != 'x' and n.strip() != 'o':
            n = input("Please enter 'x' or 'o':")
        m = input("Please enter position y:")
        p = input("Please enter position x:")
        if int(m)-1 < len(board) and int(p)-1 < len(board):
            board[int(m)-1][int(p)-1] = n
        printBoard(board)
        x = checkWin(n,board)
    w = input("rematch? yes?: ")
    if w == "yes":
        game()
    else:
        print("FINE THEN")
        print("GOOD GAME BISH!!!!")
    
#message after user chooses the option to quit the game        
def quitGame():
    print("Hope you had fun!!")
    
#first initialized as the game's main menu    
print("Tic Tac Toe")
print("play")
print("quit")
a = input("Chose: ")
while a != "play" and a != "quit":
    a = input("Chose: ")
    
if a == "play":
    game()
elif a == "quit":
    quitGame()
    
        
    
    
    
    
