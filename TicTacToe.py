class TicTacToe:
    def __int__(self):
        pass

    def printBoard(self, board):
        print('------------------')
        for row in board:
            print(' ', row[0], ' | ', row[1], ' | ', row[2])
            print('------------------')

    def emptySpace(self, board):
        for row in board:
            for cell in row:
                if not cell:
                    return True
        return False

    def setState(self, cellxy, state, board):
        x = int(cellxy[0]) - 1
        y = int(cellxy[1]) - 1
        row = board[x]
        cell = row[y]
        if not cell:
            board[x][y] = state
            return True
        return False

    def checkXY(self, xy):
        xy = str(xy)
        if len(xy) != 2:
            return False
        if int(xy[0]) > 3 or int(xy[0]) < 1 or int(xy[1]) > 3 or int(xy[1]) < 1:
            return False
        return True

    def checkWin(self, board):
        if board[0][0] == board[0][1] == board[0][2] != '':
            winner = board[0][0]
            print(f'{winner} won!!')

        elif board[2][0] == board[2][1] == board[2][2] != '':
            winner = board[2][0]
            print(f'{winner} won!!')

        elif board[1][0] == board[1][1] == board[1][2] != '':
            winner = board[1][0]
            print(f'{winner} won!!')

        elif board[0][0] == board[1][0] == board[2][0] != '':
            winner = board[0][0]
            print(f'{winner} won!!')

        elif board[0][1] == board[1][1] == board[2][1] != '':
            winner = board[0][1]
            print(f'{winner} won!!')

        elif board[0][2] == board[1][2] == board[2][2] != '':
            winner = board[0][2]
            print(f'{winner} won!!')

        elif board[0][0] == board[1][1] == board[2][2] != '':
            winner = board[0][0]
            print(f'{winner} won!!')

        elif board[0][2] == board[1][1] == board[2][0] != '':
            winner = board[0][2]
            print(f'{winner} won!!')

        else:
            return False
        return True


turn = 'x'
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
        ]
game = TicTacToe()

while game.emptySpace(board):
    game.printBoard(board)
    print()
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    print(f'{turn}\'s Turn')
    while True:
        xy = int(input('Enter coordinates of your mark:'))
        if game.checkXY(xy):
            if game.setState(str(xy), turn, board):
                break
            print('This cell is already full')
            continue
        print('Error!!')
        continue
    if game.checkWin(board):
        break
game.printBoard(board)
game.checkWin(board)
print('Game Over!!')