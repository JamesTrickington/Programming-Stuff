from random import randint
from time import sleep
import time
import sys

class c:
    FLASH = '\033[5m'
    bYELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;34m'
    bYELLOW = '\033[1;33m'
    WR = '\033[97;41m'
    WB = '\033[97;104m'
    BLUE = '\033[0;34m'
    bBLUE = '\033[1;94m'
    RED ='\033[0;31m'
    bRED = '\033[1;31m'
    gRED = '\033[41m'
    GREEN = '\033[0;92m'
    bGREEN = '\033[1;32m'
    gGREEN = '\033[42m'
    PURPLE = '\033[0;35m'
    bPURPLE = '\033[1;35m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


board = [
        ['  ','1','2','3','4','5','6','7','8','9','10'],
        [' 1','X','X','X','X','X','X','X','X','X','X'],
        [' 2','X','X','X','X','X','X','X','X','X','X'],
        [' 3','X','X','X','X','X','X','X','X','X','X'],
        [' 4','X','X','X','X','X','X','X','X','X','X'],
        [' 5','-','-','O','O','-','-','O','O','-','-'],
        [' 6','-','-','O','O','-','-','O','O','-','-'],
        [' 7','6','2','2','2','6','2','3','5','6','M'],
        [' 8','5','B','B','4','2','9','8','8','2','4'],
        [' 9','2','5','4','B','5','6','S','7','2','7'],
        ['10','3','B','B','F','B','4','3','3','3','7']
        ]

rBoard = [
        ['  ','1','2','3','4','5','6','7','8','9','10'],
        [' 1','3','B','B','F','B','4','3','3','3','7'],
        [' 2','2','5','4','B','5','6','S','7','2','7'],
        [' 3','5','B','B','4','2','9','8','8','2','4'],
        [' 4','6','2','2','2','6','2','3','5','6','M'],
        [' 5','-','-','O','O','-','-','O','O','-','-'],
        [' 6','-','-','O','O','-','-','O','O','-','-'],
        [' 7','E','E','E','E','E','E','E','E','E','E'],
        [' 8','E','E','E','E','E','E','E','E','E','E'],
        [' 9','E','E','E','E','E','E','E','E','E','E'],
        ['10','E','E','E','E','E','E','E','E','E','E']
        ]

sBoard = [
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         ]

success = False

def resetSBoard():
    sBoard = [
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         [''],
         ]

def styleBoard(board):
    resetSBoard()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == 0 or row == 0:
                sBoard[col].append(board[col][row])
            elif rBoard[col][row] not in ['-','E','O']:
                sBoard[col].append(c.bRED + board[col][row] + c.ENDC)
            elif board[col][row] == 'O':
                sBoard[col].append(c.bBLUE + board[col][row] + c.ENDC)
            elif board[col][row] == '-':
                sBoard[col].append(c.bGREEN + board[col][row] + c.ENDC)
            elif board[col][row] == 'F':
                sBoard[col].append(c.bYELLOW + board[col][row] + c.ENDC)
            elif rBoard[col][row] == 'E':
                sBoard[col].append(c.bPURPLE + board[col][row] + c.ENDC)

def printBoard(board):
    styleBoard(board)
    for row in sBoard:
        print  "    ".join(row)
        print " "
        time.sleep(.2)

printBoard(board)

def checkRank(nR,nC,r,c):
    try:
        enemy = int(rBoard[nR][nC])
    except:
        enemy = rBoard[nR][nC]
    
    try:
        ally = int(board[r][c])
    except:
        ally = board[r][c]
    
    if enemy.type() == str:
        if enemy == 'B':
            if ally == 3:
                board[nR][nC] = '3'
                board[r][c] = '-'
                rBoard[nR][nC] = 'E'
                rBoard[r][c] = '-'
                success = True
                sys.stderr.write("\x1b[2J\x1b[H")
                print "It was a Bomb. Your Miner defused it!"
                time.sleep(2)
            else:
                board[nR][nC] = 'B'
                board[r][c] = '-'
                rBoard[r][c] = '-'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "It was a Bomb. Your troop was blown to bits."
                time.sleep(2)
        
        elif enemy == 'M':
            if ally == 'M':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = '-'
                rBoard[nR][nC] = '-'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Marshall too! They were both slain."
                time.sleep(2)
            elif ally == 'S':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'S'
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Marshall. Your Scout has defeated him."
                time.sleep(2)
            else:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'M'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Marshall! He has slain your troop."
                time.sleep(2)
        
        elif enemy == 'S':
            if ally == 'M':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'S'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Scout! Your Marshall has been slain."
                time.sleep(2)
            elif ally == 'S':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = '-'
                rBoard[nR][nC] = '-'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Scout too! They were both slain."
                time.sleep(2)
            elif ally > 2:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = str(ally)
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Scout! Your peice won because of its higher rank."
                time.sleep(2)
            else:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'S'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Scout! Your peice lost because of its lower rank."
                time.sleep(2)
        
        # ~ elif enemy == 'F':
            
        
    elif enemy.type() == int:
        if ally.type() == str:
            if ally == 'M':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'M'
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                "The enemy was a lower rank. Your Marshall won!"
                time.sleep(2)
            elif ally == 'S':
                if enemy > 2:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(enemy)
                    sys.stderr.write("\x1b[2J\x1b[H")
                    "The enemy was a higher rank! Your Scout has been slain."
                    time.sleep(2)
                elif enemy < 2:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(ally)
                    rBoard[nR][nC] = 'E'
                    sys.stderr.write("\x1b[2J\x1b[H")
                    "The enemy was a lower rank. Your Scout won!"
                    time.sleep(2)
        elif ally.type() == int:
            if enemy > ally:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(enemy)
                    sys.stderr.write("\x1b[2J\x1b[H")
                    "The enemy was a higher rank! Your Troop has been slain."
                    time.sleep(2)
                elif enemy < ally:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(ally)
                    rBoard[nR][nC] = 'E'
                    sys.stderr.write("\x1b[2J\x1b[H")
                    "The enemy was a lower rank. Your Troop won!"
                    time.sleep(2)
            

def movePeice(r,c,d):
    try:
        r = int(r)
        c = int(c)
    
    except:
        success = False
        sys.stderr.write("\x1b[2J\x1b[H")
        print "\nValues must be numbers!\n"
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")
    
    if r not in range(len(board)) or c not in range(len(board)) or r==0 or c==0:
        success = False
        sys.stderr.write("\x1b[2J\x1b[H")
        print "\nThat's not even on the board!\n"
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")
    
    elif board[r][c] in ['O','-', 'F', 'B']:
        success = False
        sys.stderr.write("\x1b[2J\x1b[H")
        print '\nThere\'s no movable peice in that location!\n'
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")
    
    elif rBoard[r][c] not in ['-','E','O']:
        success = False
        sys.stderr.write("\x1b[2J\x1b[H")
        print '\nThat\'s not your peice!\n'
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")
    
    elif d.title() == 'N':
        nR = r - 1
        nC = c
        if rBoard[nR][nC] in ['E','O'] or nR not in range(len(board)) or nC not in range(len(board)):
            success = False
            sys.stderr.write("\x1b[2J\x1b[H")
            print "\nYou can't move that there!\n"
            time.sleep(1)
            sys.stderr.write("\x1b[2J\x1b[H")
            
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            success = True
            sys.stderr.write("\x1b[2J\x1b[H")
    
    elif d.title() == 'E':
        nR = r
        nC = c + 1
        if rBoard[nR][nC] in ['E','O'] or nR not in range(len(board)) or nC not in range(len(board)):
            print '\nYou can\'t move that there!\n'
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            success = True
            sys.stderr.write("\x1b[2J\x1b[H")
    
    elif d.title() == 'S':
        nR = r + 1
        nC = c
        if rBoard[nR][nC] in ['E','O'] or nR not in range(len(board)) or nC not in range(len(board)):
            sys.stderr.write("\x1b[2J\x1b[H")
            print "\nYou can't move that there!\n"
            time.sleep(1)
            sys.stderr.write("\x1b[2J\x1b[H")
        elif rBoard[nR][nC] not in ['E','-','O']:
            checkRank(nR,nC,r,c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            success = True
            sys.stderr.write("\x1b[2J\x1b[H")
    
    elif d.title() == 'W':
        nR = r
        nC = c - 1
        if rBoard[nR][nC] in ['E','O'] or nR not in range(len(board)) or nC not in range(len(board)):
            print "\nYou can't move that there!\n"
        elif rBoard[nR][nC] not in ['E','-','O']:
            checkRank(nR,nC,r,c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            success = True
            sys.stderr.write("\x1b[2J\x1b[H")
    # ~ printBoard(board)


def checkQuit(var):
    if var.title() == 'Q':
        sys.exit()

peiceRow = ''
peiceCol = ''

while peiceRow.title() != 'Q' and peiceCol.title() != 'Q':
    peiceRow = raw_input('Choose the ROW the desired peice is in:  ')
    checkQuit(peiceRow)
    
    peiceCol = raw_input('Choose the COLLUMN the desired peice is in:  ')
    checkQuit(peiceCol)
    
    direction = raw_input('Choose the DIRECTION you want to move it in (NESW):  ')
    checkQuit(direction)
    
    movePeice(peiceRow,peiceCol,direction)
    
    print ''
    for row in board:
        print  "    ".join(row)
        print " "
        time.sleep(.2)
