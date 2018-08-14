from random import randint
from time import sleep
import time
import sys


class c:  # For coloring the board
    FLASH = '\033[5m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;34m'
    bYELLOW = '\033[1;33m'
    WR = '\033[97;41m'
    WB = '\033[97;104m'
    BLUE = '\033[0;34m'
    bBLUE = '\033[1;94m'
    RED = '\033[0;31m'
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


board = [  # The board as seen by player
    ['  ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    [' 1', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [' 2', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [' 3', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [' 4', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [' 5', '-', '-', 'O', 'O', '-', '-', 'O', 'O', '-', '-'],
    [' 6', '-', '-', 'O', 'O', '-', '-', 'O', 'O', '-', '-'],
    [' 7', '6', '2', '2', '2', '6', '2', '3', '5', '6', 'M'],
    [' 8', '5', 'B', 'B', '4', '2', '9', '8', '8', '2', '4'],
    [' 9', '2', '5', '4', 'B', '5', '6', 'S', '7', '2', '7'],
    ['10', '3', 'B', 'B', 'F', 'B', '4', '3', '3', '3', '7']
]

rBoard = [  # The board as seen by enemy
    ['  ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    [' 1', '7', '3', '3', '3', '4', 'B', 'F', 'B', 'B', '3'],
    [' 2', '7', '2', '7', 'S', '6', '5', 'B', '4', '5', '2'],
    [' 3', '4', '2', '8', '8', '9', '2', '4', 'B', 'B', '5'],
    [' 4', 'M', '6', '5', '3', '2', '6', '2', '2', '2', '6'],
    [' 5', '-', '-', 'O', 'O', '-', '-', 'O', 'O', '-', '-'],
    [' 6', '-', '-', 'O', 'O', '-', '-', 'O', 'O', '-', '-'],
    [' 7', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    [' 8', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    [' 9', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ['10', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
]

sBoard = [  # The stylized board
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', ''],
]


def styleBoard(board):
    """
    Stylizes the board and adds color.
    Makes it easier to tell what peices are yours and and enemy's

    :param board: The board you are trying to add color to
    :return: Nothing
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == 0 or row == 0:
                sBoard[col][row] = board[col][row]
            elif rBoard[col][row] not in ['-', 'E', 'O']:
                sBoard[col][row] = c.bRED + board[col][row] + c.ENDC
            elif board[col][row] == 'O':
                sBoard[col][row] = c.bBLUE + board[col][row] + c.ENDC
            elif board[col][row] == '-':
                sBoard[col][row] = c.bGREEN + board[col][row] + c.ENDC
            elif board[col][row] == 'F':
                sBoard[col][row] = c.bYELLOW + board[col][row] + c.ENDC
            elif rBoard[col][row] == 'E':
                sBoard[col][row] = c.bPURPLE + board[col][row] + c.ENDC


def printBoard():
    """
    Prints the stylized board all formatted and spaced out

    :return: Nothing
    """
    styleBoard(board)
    print ""
    for row in sBoard:
        print  "    ".join(row)
        print " "
        time.sleep(.1)


def movePeice(r, c, d):
    """
    Moves the selected piece in the selected direction if there is no conflict,
    otherwise tells you you can't move there or calls checkRank()

    :param r: Row - the row the piece you want to move is in
    :param c: Column - the column the piece you want to move is  in
    :param d: Direction - the compass direction you want to move the piece in (N,E,S,W)
    :return: Nothing
    """
    try:
        r = int(r)
        c = int(c)

    except:
        sys.stderr.write("\x1b[2J\x1b[H")
        print "\nValues must be numbers!\n"
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")

    if r not in range(len(board)) or c not in range(len(board)) or r == 0 or c == 0:
        sys.stderr.write("\x1b[2J\x1b[H")
        print "\nThat's not even on the board!\n"
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")

    elif board[r][c] in ['O', '-', 'F', 'B']:
        sys.stderr.write("\x1b[2J\x1b[H")
        print '\nThere\'s no movable peice in that location!\n'
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")

    elif rBoard[r][c] not in ['-', 'E', 'O']:
        sys.stderr.write("\x1b[2J\x1b[H")
        print '\nThat\'s not your peice!\n'
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'N':
        nR = r - 1
        nC = c
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            sys.stderr.write("\x1b[2J\x1b[H")
            print "\nYou can't move that there!\n"
            time.sleep(1)
            sys.stderr.write("\x1b[2J\x1b[H")
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'E':
        nR = r
        nC = c + 1
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            print '\nYou can\'t move that there!\n'
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'S':
        nR = r + 1
        nC = c
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            sys.stderr.write("\x1b[2J\x1b[H")
            print "\nYou can't move that there!\n"
            time.sleep(1)
            sys.stderr.write("\x1b[2J\x1b[H")
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'W':
        nR = r
        nC = c - 1
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            print "\nYou can't move that there!\n"
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")
    printBoard()


def checkRank(nR, nC, r, c):
    """
    Checks the ranks of the two opposing pieces, responds accordingly.

    :param nR: New Row - the row you're moving the piece to
    :param nC: New Column - the column you're moving the piece to
    :param r: Row - the row the peice you're moving is in
    :param c: Column - the column the peice you're moving is in
    :return: Nothing
    """
    try:
        enemy = int(rBoard[nR][nC])
    except:
        enemy = rBoard[nR][nC]

    try:
        ally = int(board[r][c])
    except:
        ally = board[r][c]

    if type(enemy) == str:
        if enemy == 'B':
            if ally == 3:
                board[nR][nC] = '3'
                board[r][c] = '-'
                rBoard[nR][nC] = 'E'
                rBoard[r][c] = '-'
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
                print "The enemy was a Scout! Your piece won because of its higher rank."
                time.sleep(2)
            else:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'S'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Scout! Your piece lost because of its lower rank."
                time.sleep(2)

        elif enemy == 'F':
            sys.stderr.write("\x1b[2J\x1b[H")

    elif type(enemy) == int:
        if type(ally) == str:
            if ally == 'M':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'M'
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a lower rank. Your Marshall won!"
                time.sleep(2)
            elif ally == 'S':
                if enemy > 2:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(enemy)
                    sys.stderr.write("\x1b[2J\x1b[H")
                    print "The enemy was a higher rank! Your Scout has been slain."
                    time.sleep(2)
                elif enemy < 2:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(ally)
                    rBoard[nR][nC] = 'E'
                    sys.stderr.write("\x1b[2J\x1b[H")
                    print "The enemy was a lower rank. Your Scout won!"
                    time.sleep(2)
        elif type(ally) == int:
            if enemy > ally:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = str(enemy)
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a higher rank! Your Troop has been slain."
                time.sleep(2)
            elif enemy < ally:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = str(ally)
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a lower rank. Your Troop won!"
                time.sleep(2)
            elif enemy == ally:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = '-'
                rBoard[nR][nC] = '-'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was the same rank! They both perished."
                time.sleep(2)


def EmovePeice(r, c, d):
    """
    Moves the enemy piece in the selected direction if there is no conflict,
    otherwise tells you you can't move there or calls checkRank()

    :param r: Row - the row the piece you want to move is in
    :param c: Column - the column the piece you want to move is  in
    :param d: Direction - the compass direction you want to move the piece in (N,E,S,W)
    :return: Nothing
    """
    try:
        r = int(r)
        c = int(c)

    except:
        sys.stderr.write("\x1b[2J\x1b[H")
        print "\nValues must be numbers!\n"
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")

    if board[r][c] in ['O', '-', 'F', 'B']:
        raise ValueError('can\'t do that')

    elif rBoard[r][c] in ['-', 'E', 'O']:
        raise ValueError('can\'t do that')

    elif d.title() == 'N':
        nR = r - 1
        nC = c
        if rBoard[nR][nC] not in ['E', '-'] or nR not in range(len(board)) or nC not in range(len(board)):
            raise ValueError('can\'t do that')
        elif rBoard[nR][nC] == 'E':
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'E':
        nR = r
        nC = c + 1
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            print '\nYou can\'t move that there!\n'
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'S':
        nR = r + 1
        nC = c
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            sys.stderr.write("\x1b[2J\x1b[H")
            print "\nYou can't move that there!\n"
            time.sleep(1)
            sys.stderr.write("\x1b[2J\x1b[H")
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")

    elif d.title() == 'W':
        nR = r
        nC = c - 1
        if rBoard[nR][nC] in ['E', 'O'] or nR not in range(len(board)) or nC not in range(len(board)):
            print "\nYou can't move that there!\n"
        elif rBoard[nR][nC] not in ['E', '-', 'O']:
            checkRank(nR, nC, r, c)
        else:
            board[nR][nC] = str(board[r][c])
            board[r][c] = '-'
            rBoard[nR][nC] = str(rBoard[r][c])
            rBoard[r][c] = '-'
            sys.stderr.write("\x1b[2J\x1b[H")
    printBoard()


def EcheckRank(nR, nC, r, c):
    """
    Checks the ranks of the two opposing pieces, responds accordingly.

    :param nR: New Row - the row you're moving the piece to
    :param nC: New Column - the column you're moving the piece to
    :param r: Row - the row the peice you're moving is in
    :param c: Column - the column the peice you're moving is in
    :return: Nothing
    """
    try:
        enemy = int(rBoard[nR][nC])
    except:
        enemy = rBoard[nR][nC]

    try:
        ally = int(board[r][c])
    except:
        ally = board[r][c]

    if type(enemy) == str:
        if enemy == 'B':
            if ally == 3:
                board[nR][nC] = '3'
                board[r][c] = '-'
                rBoard[nR][nC] = 'E'
                rBoard[r][c] = '-'
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
                print "The enemy was a Scout! Your piece won because of its higher rank."
                time.sleep(2)
            else:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'S'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a Scout! Your piece lost because of its lower rank."
                time.sleep(2)

        elif enemy == 'F':
            sys.stderr.write("\x1b[2J\x1b[H")

    elif type(enemy) == int:
        if type(ally) == str:
            if ally == 'M':
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = 'M'
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a lower rank. Your Marshall won!"
                time.sleep(2)
            elif ally == 'S':
                if enemy > 2:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(enemy)
                    sys.stderr.write("\x1b[2J\x1b[H")
                    print "The enemy was a higher rank! Your Scout has been slain."
                    time.sleep(2)
                elif enemy < 2:
                    board[r][c] = '-'
                    rBoard[r][c] = '-'
                    board[nR][nC] = str(ally)
                    rBoard[nR][nC] = 'E'
                    sys.stderr.write("\x1b[2J\x1b[H")
                    print "The enemy was a lower rank. Your Scout won!"
                    time.sleep(2)
        elif type(ally) == int:
            if enemy > ally:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = str(enemy)
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a higher rank! Your Troop has been slain."
                time.sleep(2)
            elif enemy < ally:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = str(ally)
                rBoard[nR][nC] = 'E'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was a lower rank. Your Troop won!"
                time.sleep(2)
            elif enemy == ally:
                board[r][c] = '-'
                rBoard[r][c] = '-'
                board[nR][nC] = '-'
                rBoard[nR][nC] = '-'
                sys.stderr.write("\x1b[2J\x1b[H")
                print "The enemy was the same rank! They both perished."
                time.sleep(2)