X = 'X'
O = 'O'
BLANK = '_'

def toogle(player):
 if player == X:
  return O
 else:
  return X

def win(player,board):
 won = ((board[0][0] == player and board[0][1] == player and board[0][2] == player)
        or
        (board[1][0] == player and board[1][1] == player and board[1][2] == player)
        or
        (board[2][0] == player and board[2][1]== player and board[2][2] == player)
        or
        (board[0][0] == player and board[1][0] == player and board[2][0] == player)
        or
        (board[0][1] == player and board[1][1] == player and board[2][1] == player)
        or
        (board[0][2] == player and board[1][2] == player and board[2][2] == player)
        or
        (board[0][0] == player and board[1][1] == player and board[2][2] == player)
        or
        (board[0][2] == player and board[1][1] == player and board[2][0] == player))
 return won

def tie(board):
 for r in range(3):
   for c in range(3):
     if board[r][c] == BLANK:
      return False
 return True

def main():
 board = [[BLANK,BLANK,BLANK],
          [BLANK,BLANK,BLANK],
          [BLANK,BLANK,BLANK]]
 print('Welcome to Tic Tac Toe! X moves first.')
 player = X
 for row in board:
  print(row)
 while not win(X, board) or win(O, board) or tie(board):
   row = int(input(f"What row for {player}'s move?"))
   col = int(input(f"What col for {player}'s move?"))
   board[row][col] = player
   for row in board:
    print(row)
   if tie(board):
    print("It's a tie!")
   elif win(X, board) or win(O, board):
    print(f'Yay {player} is the winner!')
   else:
    player = toogle(player)

if __name__ == "__main__":
    main()






