from random import randint
from time import sleep
import time
import sys

restartQuit = ''

while True:
    if restartQuit.strip().title() == 'Q':
        break
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
    
    restartLoop = False
    itteration = True
    developer = False
    
    def printStartScreen():
        print '\n'
        for c in 'BattleShip':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
        print'\n'
    printStartScreen()
    sleep(.25)
    raw_input('Press enter to start...\n')
    sleep(.25)
    
    developer = raw_input('Developer settings?(Y/N)')
    developer = developer.strip()
    if developer.title() == 'Y':
        developer = True
        print ''
    elif developer.title() == 'N':
        developer = False
        print ''
    else:
        print "\nI guess I'll take that as a No(Not Y or N).\n"
        developer = False
        
    sleep(1)
    
    while itteration:
        def printBoard(board):
            print 'Enter "q" at any time to quit.'
            for row in board:
                print " ".join(row)
        def testPrintBoard(board):
            sys.stdout.write('Enter "q" at any time to quit.')
            sys.stdout.flush()
            time.sleep(.03)
            for row in board:
                for item in row:
                    sys.stdout.write(item)
                    sys.stdout.flush()
                    time.sleep(.01)
                    sys.stdout.write(' ')
                    sys.stdout.flush()
                    time.sleep(.03)
                time.sleep(.03)
                print ''
        def newPrintBoard(board):
            print 'Enter "q" at any time to quit.'
            for row in board:
                print " ".join(row)
                time.sleep(.2)
    
        sleep(.25)
        newPrintBoard(board)
        
        if developer:
            sleep(.2)
            print ship_col
            sleep(.2) 
            print ship_row 
        #Developer tool, just shows ship location
        
        col_guess = raw_input('\nGuess a collumn: ')
        if col_guess.strip().title() == 'Q':
            break
        row_guess = raw_input('\nGuess a row: ')
        if row_guess.strip().title() == 'Q':
            break
    
        print '\nYou guessed %s, %s.' %(col_guess, row_guess)
    
        sleep(.25)
        
        if not col_guess or not row_guess:
            print "\nYou didn't enter a required value.\n\nTry again.\n"
            sleep(.25)
        elif int(row_guess) == ship_row and int(col_guess) == ship_col:
            itteration = False
            sleep(.25)
        elif not int(row_guess) in range(1,8) or not int(
                                                col_guess) in range(1,8):
                print "\nThat's not even in the ocean! Try again.\n"
                sleep(.25)
        elif board[int(row_guess)][int(col_guess)] == '-':
            print '\nYou already guessed that. Try again.\n'
            sleep(.25)
        else:
            board[int(row_guess)][int(col_guess)] = '-'
            print '\nYou missed. Try again.\n'
            sleep(.25)
    
    if itteration == False:
        print '\nCongradulations! You hit the ship!\n'
        sleep(.5)
        board[ship_row][ship_col] = 'X' 
        print "This was your final board:"
        sleep(.25)
        newPrintBoard(board)
        sleep(.25)
        print '\nThe Ship was at %s, %s.\n' %(col_guess, row_guess)
        restartLoop = True
        
        while restartLoop == True:
            restartQuit = raw_input("\nEnter R to restart or Q to quit.\n")
            if restartQuit.strip().title() == 'R':
                itteration = True
                restartLoop = False
                break
            elif restartQuit.strip().title() =='Q':
                restartLoop = False
                break
            else:
                print 'Answer must be either R or Q.\n'
