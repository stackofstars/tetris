#test file2
import pieces
import random

score = 0
level = 1
time = 1
gameOver = False
boardrows = 20
boardcols = 10
blocks = ["J", "L", "I", "S", "T", "Z", "O"]
count = 0
board = [[0 for i in range(boardcols)] for j in range(boardrows)] #creating the game board

def printBoard(x): #print the board
    for row in x:
        print(row)

def main():
    while GameOver == False:
        if:
            gameOver = True
        else:
            for x in board[0]:
                if x != 0:
                    count += 1
                if count == boardcols:
                    clearRow()
                    moveDown()
                    count = 0

            pieces(random.choice(blocks))

def levelUp():
    level += 1

def moveDown():

def clearRow():
