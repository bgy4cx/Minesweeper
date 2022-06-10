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
    return -1
