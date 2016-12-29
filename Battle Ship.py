#ship battle game

from random import randint

#create empty list
board = []

#add 5 rows of 5 O's into the list
for x in range(0, 5):
    board.append(["O"] * 5)

#printing the O's from the list without the quotation sign
def print_board(board):
    for row in board:
        print " ".join(row)

#calling the print board function to see the intial board
print_board(board)

#assigning random numbers within the limits of board for the actual location of ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#assinging the random numbers to var's 
ship_row = random_row(board)
ship_col = random_col(board)

#printing the answer to debug our code as we make it
print ship_row
print ship_col


# Write your code below!
#if the guess is right

for turn in range(4):
    print "Turn" , (turn + 1)
    #grabbing the users guess
    if turn < 4:

        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        #checking inputs with answer
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sank my battleship!"
            #incase guessed right, you dont want to continue guessing
            break

        else:
            
            #outside of the 5x5
            if guess_row not in range(5) or guess_col not in range(5):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == 'X' :
                print "You guessed that one already. Try again"
                turn -= 1
            else:
                print "You missed my battleship!"
                #print an X where the users guess is
                #raw input turns into string format, we convert to int for list indexing
                board[int(guess_row)][int(guess_col)] = 'X'
                print_board(board)
            if turn == 3:
                print "Game Over"



                
        

        