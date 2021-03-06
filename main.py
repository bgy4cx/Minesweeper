#It draws the game board with the necessary values.
def drawboard(board):
    cannot_draw = False     
    d_board = list(map(list, board))
    try:
        for i in range(3):
            for j in range(3):
                if board[i][j] == "B":
                    d_board[i][j] = " "
                if board[i][j] == "FB":
                    d_board[i][j] = "F"
        f_row = "|"+d_board[0][0]+"|"+d_board[0][1]+"|"+d_board[0][2]+"|\n"
        s_row = "|"+d_board[1][0]+"|"+d_board[1][1]+"|"+d_board[1][2]+"|\n"
        t_row = "|"+d_board[2][0]+"|"+d_board[2][1]+"|"+d_board[2][2]+"|\n"
        print("",f_row, s_row, t_row,"", sep="+-+-+-+\n")
    except:
        cannot_draw = True    
    return True if cannot_draw == False else False

# If no empty square the player win.
def checkWinner(board):
    win = True
    print(board)
    for i in range(len(board[0])):
        for j in range(len(board[0][0])):
            if board[i][j] == " ":
                win = False
                break
    return win

# It clear the empty squares where no bomb in the neighbourhood.
def clearNeighbours(board):
    for i in range(9):
        for i in range(3):
            for j in range(3):
                if i<2 and board[i][j] == "_" and board[i+1][j] == " ":
                    board[i+1][j] = "_"
                if j<2 and i<2 and board[i][j] == "_" and board[i+1][j+1] == " ":
                    board[i+1][j+1] = "_"
                if j<2 and board[i][j] == "_" and board[i][j+1] == " ":
                    board[i][j+1] = "_"
                if i>0 and board[i][j] == "_" and board[i-1][j] == " ":
                    board[i-1][j] = "_"
                if  j>0 and i>0 and board[i][j] == "_" and board[i-1][j-1] == " ":
                    board[i-1][j-1] = "_"
                if  j>0 and board[i][j] == "_" and board[i][j-1] == " ":
                    board[i][j-1] = "_"
                if j>0 and i<2 and board[i][j] == "_" and board[i+1][j-1] == " ":
                    board[i+1][j-1] = "_"
                if i>0 and j<2 and board[i][j] == "_" and board[i-1][j+1] == " ":
                    board[i-1][j+1] = "_"
    return board

# It shows information about the number of the bombs in the neighbourhood.
def checkBombs(board):
    for i in range(3):
        for j in range(3):
            c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = False
            if board[i][j] != "B" and board[i][j] != "X" and board[i][j] != "F" and board[i][j] != "FB" and board[i][j] != " ":
                board[i][j] = "_"
                for c in range(9):
                    if i<2 and board[i+1][j] in ["B", "FB"] and c1 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        #The below part is not needed because it is the first condition:    
                        #else:
                        #    board[i][j] = str(int(board[i][j]) + 1)
                        c1 = True                       
                    if j<2 and i<2 and board[i+1][j+1] in ["B", "FB"] and c2 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c2 = True
                    if j<2 and board[i][j+1] in ["B", "FB"] and c3 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c3 = True
                    if i>0 and board[i-1][j] in ["B", "FB"] and c4 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c4 = True
                    if  j>0 and i>0 and board[i-1][j-1] in ["B", "FB"] and c5 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c5 = True
                    if  j>0 and board[i][j-1] in ["B", "FB"] and c6 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1)
                        c6 = True
                    if j>0 and i<2 and board[i+1][j-1] in ["B", "FB"] and c7 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c7 = True
                    if i>0 and j<2 and board[i-1][j+1] in ["B", "FB"] and c8 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c8 = True
    return board

# It can remove the flag too if it is needed.
def addFlag(board, square):
    if board[square[0]][square[1]] == "B":
        board[square[0]][square[1]] = "FB"
    elif board[square[0]][square[1]] == "FB":
        board[square[0]][square[1]] = "B"
    elif board[square[0]][square[1]] == " ":
        board[square[0]][square[1]] = "F"
    elif board[square[0]][square[1]] == "F":
        board[square[0]][square[1]] = " "
    return board

def doStep(board, step):
    if board[step[0]][step[1]] == "B":
        board[step[0]][step[1]] = "X"
    if board[step[0]][step[1]] == " ":      
        board[step[0]][step[1]] = "_"
    return board

#It is the main function.
def minesweeper(board, sign, square):
    if sign == "S":
        doStep(board, square)
        clearNeighbours(board)
        checkBombs(board)
        drawboard(board)
        if board[square[0]][square[1]] == "X":
            print("You are lose! :(")
            return "Lose"
        elif checkWinner(board):
            print("You are win! :)")
            return "Win"
        else:
            print("Done. Next step pls!")
            return "Next"
    if sign == "F":
        addFlag(board, square)
        drawboard(board)
        print("Done. Next step pls!")
        return "Next"

#minesweeper([['B','B','B'], ['B',' ','B'], ['B','B','B']],"S",[1,1])
#minesweeper([['B','B','B'], ['B',' ','B'], ['B','B','B']],"S",[0,0])
#minesweeper([[' ',' ',' '], [' ',' ',' '], [' ',' ','B']],"S",[1,1])
#minesweeper([[' ',' ',' '], ['B','B','B'], [' ',' ','B']],"S",[2,1])
#minesweeper([[' ',' ',' '], ['B','B','B'], ['_','_','B']],"F",[2,2])

# A simple game:
gameboard = [[' ','B','B'], ['B','B',' '], ['B',' ',' ']]
minesweeper(gameboard,"S",[2,2])
minesweeper(gameboard,"F",[1,1])
minesweeper(gameboard,"F",[0,1])
minesweeper(gameboard,"F",[0,2])
minesweeper(gameboard,"F",[1,0])
minesweeper(gameboard,"F",[2,0])
minesweeper(gameboard,"S",[0,0])