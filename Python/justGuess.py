from time import sleep
import sys

class bcolors:
    FLASH = '\033[5m'
    YELLOW = '\033[0;33m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;34m'
    WR = '\033[97;41m'
    BLUE = '\033[0;34m'
    bBLUE = '\033[1;94m'
    RED ='\033[0;31m'
    bRED = '\033[1;31m'
    gRED = '\033[41m'
    GREEN = '\033[0;92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def slow_delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.25)

def fast_delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.1)

def med_delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.15)

def noGuessBranch(counter):
    if counter == 4:
        sys.stderr.write("\x1b[2J\x1b[H")
        sleep(1)
        slow_delay_print( bcolors.RED+'Okay\n\n\n')
        sleep(.75)
        fast_delay_print(
           'Okay, haha funny. Hilarious, I get it, it\'s a funny joke.'
            +' Now please, please stop. Okay?\n\n'+bcolors.ENDC
            )
        sleep(1.5)
        
    elif counter == 5:
        sys.stderr.write("\x1b[2J\x1b[H")
        sleep(1)
        slow_delay_print(bcolors.bRED+'Cut the crap.\n\n\n'+bcolors.ENDC)
        sleep(.75)
        fast_delay_print(
             bcolors.RED+'I put all this work into creating a game for you'
            +' and THIS is what I get in return?\n\n'
            )
        sleep(.5)
        fast_delay_print(
            'Quit your stupid BS and PLAY THE F**KING GAME!!!\n\n'
        )
        sleep(1)
        med_delay_print('Okay, just\n\nI\'m sorry, let\'s Just try this again.'+bcolors.ENDC)
        sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")
    elif counter == 6:
        sys.stderr.write("\x1b[2J\x1b[H")
        fast_delay_print(
            bcolors.RED+'Nope, nope, nope, nope, nope, nope, nope, nope, nope, nope, nope.\n\n\n'
        )
        sleep(1)
        med_delay_print('That\'s it, I\'m done with you.'+bcolors.ENDC)
        sleep(4)
        sys.stderr.write("\x1b[2J\x1b[H")
        slow_delay_print(bcolors.bRED + '\033[32;98fGame Over\033[f' + bcolors.ENDC)
        sleep(4)
        