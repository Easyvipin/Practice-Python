# built a tic tac toe game

space_keys = list('123456789')
X, O, BLANK = 'X', 'O', ' '


def main():
    print("********** Welcome To Tic-Tac-toe Game")
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))

        move = None

        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input()
        updateBoardGame(gameBoard, move, currentPlayer)

        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isGameTie(gameBoard):
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break
            # Swap turns.
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


def getBlankBoard():
    board = {}
    for space in space_keys:
        board[space] = BLANK
    return board


def getBoardStr(board):
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'], board['8'], board['9'])


def isValidSpace(board, space):
    return space in space_keys and board[space] == BLANK


def updateBoardGame(board, move, mark):
    board[move] = mark


def isWinner(b, p):
    return((b['1'] == b['2'] == b['3'] == p) or  # Across the top
           (b['4'] == b['5'] == b['6'] == p) or  # Across the middle
           (b['7'] == b['8'] == b['9'] == p) or  # Across the bottom
           (b['1'] == b['4'] == b['7'] == p) or  # Down the left
           (b['2'] == b['5'] == b['8'] == p) or  # Down the middle
           (b['3'] == b['6'] == b['9'] == p) or  # Down the right
           (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
           (b['1'] == b['5'] == b['9'] == p))   # Diagonal


def isGameTie(board):
    for space in space_keys:
        if board[space] == BLANK:
            return False
    return True


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.
