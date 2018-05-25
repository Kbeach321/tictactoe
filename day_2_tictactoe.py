# Tic tac Toe

# Define a Board class
#
import random

class Board:
    def __init__(self, size=3):
        self.board = []
        self.size = size

        for rows in range(size):
            row = []
            for cols in range(size):
                row.append("[__]")
            self.board.append(row)

#    def winner(self):
        ###Horizontal###
#        [0][0] == [1][0] == [2][0]
#        [0][1] == [1][1] == [2][1]
#        [0][2] == [1][2] == [2][2]

        ###Vertical###
#        [0][0] == [0][1] == [0][2]
#        [1][0] == [1][1] == [1][2]
#        [2][0] == [2][1] == [2][2]

    def __str__(self):
        for row in self.board:
            print(" ".join(row))
        return ""


x = Board()
print(x)
# input == 0 0
# x.board[0][0] = "X"


players = ["X" , "O"]
current_player = players[0]

while True:
    #Player X Starts#
    print(f"Player {current_player}'s turn")
    input()
    #Switch Player System#
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    #Player O Moves#
