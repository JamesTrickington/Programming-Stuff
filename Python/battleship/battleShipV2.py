from random import randint
from time import sleep
import time
import sys

ship1x1 = ''
ship1y1= ''

ship1x2 = ''
ship1y2 = ''

ship1x3 = ''
ship1y3 = ''


board = [
        [' ','1', '2', '3', '4', '5', '6', '7'],
        ['1', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['2', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['3', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['4', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['5', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['6', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['7', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ]
def resetBoard():
    board = [
        [' ','1', '2', '3', '4', '5', '6', '7'],
        ['1', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['2', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['3', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['4', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['5', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['6', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['7', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ]
def random_row(board):
    return randint(1, len(board) - 1)
def random_col(board):
    return randint(1, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board) 

itteration = True
developer = False

def printStartScreen():
    print '\n'
    for c in 'BattleShip':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
    print '\n'
printStartScreen()
raw_input('Press enter to start...')

print'\n'
developer = raw_input('Developer settings?(Y/N)')
developer = developer.strip()
if developer.title() == 'Y':
    developer = True
elif developer.title() == 'N':
    developer = False
else:
    print "\nI guess I'll take that as a No(Not Y or N).\n"
    developer = False
    
sleep(1)

while itteration:
    def printBoard(board):
        print 'Enter "q" at any time to quit.'
        for row in board:
            print " ".join(row)

    printBoard(board)
    
    if developer:
        print ship_col 
        print ship_row 
    #Developer tool, just shows ship location
    
    col_guess = raw_input('Guess a collumn: ')
    if col_guess.strip().title() == 'Q':
        break
    row_guess = raw_input('Guess a row: ')
    if row_guess.strip().title() == 'Q':
        break

    print 'You guessed %s, %s.' %(col_guess, row_guess)

    sleep(1)
    
    if not col_guess or not row_guess:
        print "\nYou didn't enter a required value.\n\nTry again."
        sleep(.5)
    elif int(row_guess) == ship_row and int(col_guess) == ship_col:
        itteration = False
        sleep(.5)
    elif not int(row_guess) in range(1,8) or not int(
                                              col_guess) in range(1,8):
            print "\nThat's not even in the ocean! Try again.\n"
            sleep(.5)
    elif board[int(row_guess)][int(col_guess)] == '-':
        print '\nYou already guessed that. Try again.\n'
        sleep(.5)
    else:
        board[int(row_guess)][int(col_guess)] = '-'
        print '\nYou missed. Try again.\n'
        sleep(.5)

if itteration == False:
    print '\nCongradulations! You hit the ship!\n'
    sleep(.5)
    board[ship_row][ship_col] = 'X' 
    print "This was your final board:"
    printBoard(board)
    print 'The Ship was at %s, %s.' %(col_guess, row_guess)
