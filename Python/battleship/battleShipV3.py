from random import randint
from time import sleep
import time
import sys
import justGuess as jG
import shipGenerator as sG

restartQuit = ''
ngCounter = 0
counter = 0

class bcolors:
    FLASH = '\033[5m'
    YELLOW = '\033[0;33m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;34m'
    WR = '\033[97;41m'
    WB = '\033[97;104m'
    BLUE = '\033[0;34m'
    bBLUE = '\033[1;94m'
    RED ='\033[0;31m'
    bRED = '\033[1;31m'
    gRED = '\033[41m'
    GREEN = '\033[0;92m'
    gGREEN = '\033[42m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
        '''resets the board'''
    def random_row(board):
        return randint(1, len(board) - 1)
    def random_col(board):
        return randint(1, len(board[0]) - 1)
    
    ship_row = random_row(board)
    ship_col = random_col(board) 
    
    restartLoop = False
    itteration = True
    developer = False
    timesGuessed = 0
    
    def printStartScreen():
        sys.stderr.write("\x1b[2J\x1b[H")
        for c in bcolors.bBLUE + 'BattleShip' + bcolors.ENDC:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
        print'\n'
    printStartScreen()
    sleep(.25)
    raw_input(bcolors.FLASH+'Press enter to start...\n'+bcolors.ENDC)
    sleep(.25)
    sys.stderr.write("\x1b[2J\x1b[H")
    
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
    
    sys.stderr.write("\x1b[2J\x1b[H") 
    sleep(.5)
    
    while itteration:
        if restartQuit.strip().title() == 'Q':
            break
        def printBoard(board):
            print 'Enter "q" at any time to quit.'
            for row in board:
                print bcolors.BLUE + " ".join(row)
                time.sleep(.2)
            print bcolors.ENDC
    
        sleep(.25)
        printBoard(board)
        
        if developer:
            sleep(.2)
            print ship_col
            sleep(.2) 
            print ship_row 
        '''Developer tool, just shows ship location'''
        
        col_guess = raw_input('\nGuess a collumn: ')
        if col_guess.strip().title() == 'Q':
            restartQuit = 'Q'
            itteration = False
            break
        row_guess = raw_input('\nGuess a row: ')
        if row_guess.strip().title() == 'Q':
            restartQuit = 'Q'
            itteration = False
            break
        
        if col_guess and row_guess:
            print bcolors.YELLOW+'\nYou guessed %s, %s.' %(col_guess, row_guess)+bcolors.ENDC
        timesGuessed = timesGuessed + 1
    
        sleep(.25)
        
        if not col_guess or not row_guess:
            ngCounter += 1
            if ngCounter == 1:
                print bcolors.WB+"\nCome on, at least guess.\n\nTry again.\n"+bcolors.ENDC
            elif ngCounter == 2:
                print bcolors.WB+"\nReally? Again? If youre not gonna play just type q.\n\nTry again.\n"+bcolors.ENDC
            elif ngCounter == 3:
                print bcolors.WB+"\nOkay, now you're just trying to annoy me. Well, it's not gonna work.\n\n"+bcolors.ENDC
            elif ngCounter == 4 or ngCounter == 5:
                jG.noGuessBranch(ngCounter)
            elif ngCounter == 6:
                jG.noGuessBranch(ngCounter)
                restartQuit = 'Q'
                break
            sleep(2)
            
        elif int(row_guess) == ship_row and int(col_guess) == ship_col:
            itteration = False
            sleep(.25)
            
        elif not int(row_guess) in range(1,8) or not int(
                                                col_guess) in range(1,8):
                print bcolors.RED + "\nThat's not even in the ocean! Try again.\n" + bcolors.ENDC
                sleep(.25)
        elif board[int(row_guess)][int(col_guess)] == '-':
            print bcolors.RED + '\nYou already guessed that. Try again.\n' + bcolors.ENDC
            sleep(.25)
            
        else:
            board[int(row_guess)][int(col_guess)] = '-'
            print bcolors.RED + '\nYou missed. Try again.\n' + bcolors.ENDC
            sleep(.25)
            
        if ngCounter > 0:
            sleep(.5)
            print '\n'
        sleep(.5)
        sys.stderr.write("\x1b[2J\x1b[H")
    if col_guess.strip().title() == 'Q' or row_guess.strip().title() == 'Q':
        break
    
    if itteration == False:
        if ngCounter == 6:
            break
            restartLoop = False
        else:
            print bcolors.GREEN + '\nCongradulations! You hit the ship!\n' + bcolors.ENDC
            sleep(.5)
            board[ship_row][ship_col] = 'X' 
            print "This was your final board:"
            sleep(.25)
            printBoard(board)
            sleep(.25)
            print '\nThe Ship was at %s, %s.\n' %(col_guess, row_guess)
            print 'You took'+bcolors.CYAN+' %s'%(timesGuessed)+bcolors.ENDC+' guesses to find the ship.'
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
                print 'Answer must be either R or Q.'