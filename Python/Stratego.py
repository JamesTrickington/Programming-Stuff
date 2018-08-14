from random import randint
from time import sleep
import time
import sys
import movement


class c:
    FLASH = '\033[5m'
    bYELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;34m'
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


def checkQuit(var):
    """
    
    :param var: The variable that you want to check
    :return: Nothing
    """
    if var.title() == 'Q':
        sys.exit()


peiceRow = ''
peiceCol = ''

sys.stderr.write("\x1b[2J\x1b[H")
movement.printBoard()
while peiceRow.title() != 'Q' and peiceCol.title() != 'Q':
    peiceRow = raw_input('Choose the ROW the desired piece is in:  ')
    checkQuit(peiceRow)

    peiceCol = raw_input('Choose the COLUMN the desired piece is in:  ')
    checkQuit(peiceCol)

    direction = raw_input('Choose the DIRECTION you want to move it in (NESW):  ')
    checkQuit(direction)

    movement.movePeice(peiceRow, peiceCol, direction)
