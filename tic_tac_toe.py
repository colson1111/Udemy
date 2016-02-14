

board = range(9)
board = ['0','1','2','3','4','5','6','7','8']
turn = 1

def print_board():
    from IPython.display import clear_output
    clear_output()
    print board[0:3]
    print board[3:6]
    print board[6:9]
    
def check_board(board):
    '''
    Check board for a winner
    '''
    if turn <= 5:
        return "No Winner"
    elif board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]
    else:
        return "No Winner"


    
def player_quit(char):
    return char == 'q'
    
def invalid_move_check(move, board):
    return board[move] <> '%d' % move
    
print_board()

for i in range(9):  
    if turn % 2 <> 0:
        
        invalid_move = True
        
        while invalid_move:
            
            move = input('Player X Go: ')   # Player X enter a new move
            
            if player_quit(move):   # check if player is quitting
                break
            
            invalid_move = invalid_move_check(move, board) # check that move is valid
            
            if invalid_move:                        # if move is invalid, print message
                print "Please enter a valid move"
    
        board[move] ='X'
        
        print_board()
        
        turn += 1
        
        winner = check_board(board)
        
        if winner <> "No Winner":
            print "Player %s wins!!!" % winner
            break
            
    else:
        
        invalid_move = True
        
        while invalid_move:
            
            move = input('Player O Go: ')  # player O enter a new move
        
            if player_quit(move):
                break
            
            invalid_move = invalid_move_check(move, board)

            if invalid_move:
                print "Please enter a valid move"
                
        board[move] = 'O'
        
        print_board()
        
        turn += 1
        
        winner = check_board(board)
        
        if winner <> "No Winner":
            print "Player %s wins!!!" % winner
            break


        
    
    
