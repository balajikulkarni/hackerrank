not_full = 0

def DisplayBoard(board):
    print(" "+board[0]+" "+board[1]+" "+board[2])
    print(" "+board[3]+" "+board[4]+" "+board[5])
    print(" "+board[6]+" "+board[7]+" "+board[8])

def GetInput():
    try:
        data = input('Enter "X" or "O" and Index> ')
        marker,index = data.split()
        return (marker,index)
    except:
        print('Invalid Input.')
        return

def Insert_IntoBoard(board,marker,index):
    global not_full
    index  = int(index)
    #Basic Sanity
    if board[index-1] != '-':
        print('Oops..! '+str(index)+' already taken ')
        return
    if index > 9 or index <= 0:
        print('Invalid Index')
        return

    #Go to Insert
    if marker == 'x' or marker == 'o':
        board[index-1] = marker
        not_full = not_full+1
        DisplayBoard(board)
    else:
        print('Invalid Marker')
        return

def CheckWinner(board,marker):
    return ((board[0] == marker and board[1] == marker and board[2] == marker) or
            (board[3] == marker and board[4] == marker and board[5] == marker) or
            (board[6] == marker and board[7] == marker and board[8] == marker) or
            (board[0] == marker and board[3] == marker and board[6] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[0] == marker and board[4] == marker and board[8] == marker) or
            (board[2] == marker and board[4] == marker and board[6] == marker))

def StartAgain():
    print('Do you want to Play again?[yes/no] ')
    return input().lower().startswith('y')

if __name__ == '__main__':
    while True:
        board = ['-']*10
        DisplayBoard(board)
        prev =''
        cur =''
        game_on = True
        while(game_on and not_full<9 ):
            marker,index = GetInput()
            marker = marker.lower()
            cur = marker
            #Check one chance per player
            if prev!=cur:
                Insert_IntoBoard(board,marker,index)
                prev = cur
            else:
                if cur == 'x':
                    print('Its Player "O" Turn !')
                else:
                    print('Its Player "X" Turn !')

            #Check who's the winner
            if marker == 'x':
                if (CheckWinner(board,marker)):
                    game_on = False
                    print('Player X has won the game !')
                    break
            else:
                if (CheckWinner(board,marker)):
                    game_on = False
                    print('Player O has won the game !')
                    break

        print('Press "Y" to start again.')
        if not StartAgain():
            print('See you soon!')
            break
