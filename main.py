def drawboard(board):
    cannot_draw = False
    try:
        f_row = "|"+str(board[0][0])+"|"+str(board[0][1])+"|"+str(board[0][2])+"|\n"
        s_row = "|"+str(board[1][0])+"|"+str(board[1][1])+"|"+str(board[1][2])+"|\n"
        t_row = "|"+str(board[2][0])+"|"+str(board[2][1])+"|"+str(board[2][2])+"|\n"
        print("",f_row, s_row, t_row,"", sep="+-+-+-+\n")
    except:
        cannot_draw = True    
    return True if cannot_draw == False else False

def checkWinner(board):
    win = True
    for i in range(len(board[0])):
        for j in range(len(board[0][0])):
            if board[i][j] == " ":
                win = False
                break
    return win

def clearNeighbours(board):
    for i in range(9):
        for i in range(3):
            for j in range(3):
                if i<2 and board[i][j] == "_" and board[i+1][j] == " ":
                    board[i+1][j] = "_"
                    print('1: ', board)
                if j<2 and i<2 and board[i][j] == "_" and board[i+1][j+1] == " ":
                    board[i+1][j+1] = "_"
                    print('2: ', board)
                if j<2 and board[i][j] == "_" and board[i][j+1] == " ":
                    board[i][j+1] = "_"
                    print('3: ', board)
                if i>0 and board[i][j] == "_" and board[i-1][j] == " ":
                    board[i-1][j] = "_"
                    print('4: ', board)
                if  j>0 and i>0 and board[i][j] == "_" and board[i-1][j-1] == " ":
                    board[i-1][j-1] = "_"
                    print('5: ', board)
                if  j>0 and board[i][j] == "_" and board[i][j-1] == " ":
                    board[i][j-1] = "_"
                    print('6: ', board)
                if j>0 and i<2 and board[i][j] == "_" and board[i+1][j-1] == " ":
                    board[i+1][j-1] = "_"
                    print('7: ', board)
                if i>0 and j>0 and board[i][j] == "_" and board[i-1][j-1] == " ":
                    board[i-1][j-1] = "_"
                    print('8: ', board)
    print(board)
    return board

def checkBombs(board):
    for i in range(3):
        for j in range(3):
            c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = False
            if board[i][j] != "B" and board[i][j] != "F" and board[i][j] != "FB" and board[i][j] != " ":
                for c in range(9):
                    if i<2 and board[i+1][j] == "B" and c1 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1)
                        c1 = True                       
                    if j<2 and i<2 and board[i+1][j+1] == "B" and c2 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c2 = True
                    if j<2 and board[i][j+1] == "B" and c3 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c3 = True
                    if i>0 and board[i-1][j] == "B" and c4 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c4 = True
                    if  j>0 and i>0 and board[i-1][j-1] == "B" and c5 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c5 = True
                    if  j>0 and board[i][j-1] == "B" and c6 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1)
                        c6 = True
                    if j>0 and i<2 and board[i+1][j-1] == "B" and c7 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c7 = True
                    if i>0 and j>0 and board[i-1][j-1] == "B" and c8 == False:
                        if board[i][j] == "_":
                            board[i][j] = "1" 
                        else:
                            board[i][j] = str(int(board[i][j]) + 1) 
                        c8 = True
    print(board)
    return board

def addFlag(board, square):
    # It can remove the flag too if it is needed.
    if board[square[0]][square[1]] == "B":
        board[square[0]][square[1]] = "FB"
    elif board[square[0]][square[1]] == "FB":
        board[square[0]][square[1]] = "B"
    elif board[square[0]][square[1]] == " ":
        board[square[0]][square[1]] = "F"
    elif board[square[0]][square[1]] == "F":
        board[square[0]][square[1]] = " "
    return board
