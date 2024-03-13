from .terminalSize import get_terminal_size
from minidevtools import YEAR, AUTHOR, VERSION

from platform import system
from time import sleep
from sys import stdout

import random
import os



class Color:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    CGREEN2 = "\033[32m"
    CYELLOW2 = "\033[93m"
    CPURPLE2 = '\033[0;35m' 
    CCYAN2 = "\033[36m"
    ENDC = "\033[0m"

COLOR = random.choice([Color.CRED2, Color.CBLUE2, Color.CGREEN2, Color.CYELLOW2, Color.CPURPLE2, Color.CCYAN2, Color.ENDC])

XLARGE = f"""

    {COLOR}███╗   ███╗ ██╗ ███╗   ██╗ ██╗ ██████╗  ███████╗ ██╗   ██╗ ████████╗  ██████╗   ██████╗  ██╗      ███████╗
    {COLOR}████╗ ████║ ██║ ████╗  ██║ ██║ ██╔══██╗ ██╔════╝ ██║   ██║ ╚══██╔══╝ ██╔═══██╗ ██╔═══██╗ ██║      ██╔════╝
    {COLOR}██╔████╔██║ ██║ ██╔██╗ ██║ ██║ ██║  ██║ █████╗   ██║   ██║    ██║    ██║   ██║ ██║   ██║ ██║      ███████╗
    {COLOR}██║╚██╔╝██║ ██║ ██║╚██╗██║ ██║ ██║  ██║ ██╔══╝   ╚██╗ ██╔╝    ██║    ██║   ██║ ██║   ██║ ██║      ╚════██║
    {COLOR}██║ ╚═╝ ██║ ██║ ██║ ╚████║ ██║ ██████╔╝ ███████╗  ╚████╔╝     ██║    ╚██████╔╝ ╚██████╔╝ ███████╗ ███████║
    {COLOR}╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝ ╚═════╝  ╚══════╝   ╚═══╝      ╚═╝     ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝
                                                                        {Color.CCYAN2}© Copyright {YEAR}, {AUTHOR}. Version {VERSION}

    """


LARGE = f"""

    {COLOR}███╗   ███╗██╗███╗   ██╗██╗██████╗ ███████╗██╗   ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
    {COLOR}████╗ ████║██║████╗  ██║██║██╔══██╗██╔════╝██║   ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    {COLOR}██╔████╔██║██║██╔██╗ ██║██║██║  ██║█████╗  ██║   ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
    {COLOR}██║╚██╔╝██║██║██║╚██╗██║██║██║  ██║██╔══╝  ╚██╗ ██╔╝   ██║   ██║   ██║██║   ██║██║     ╚════██║
    {COLOR}██║ ╚═╝ ██║██║██║ ╚████║██║██████╔╝███████╗ ╚████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    {COLOR}╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═════╝ ╚══════╝  ╚═══╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                            {Color.CCYAN2}© Copyright {YEAR}, {AUTHOR}. Version {VERSION}
    
    """


MEDIUM = f"""

    {COLOR}███╗  ███╗█████╗ ██████╗██╗  ██╗████████╗ ████╗  ████╗ ██╗    ██████╗
    {COLOR}████╗████║██╔═██╗██╔═══╝██║  ██║╚══██╔══╝██╔═██╗██╔═██╗██║    ██╔═══╝
    {COLOR}██╔███╔██║██║ ██║████╗  ██║  ██║   ██║   ██║ ██║██║ ██║██║    ██████╗
    {COLOR}██║╚█╔╝██║██║ ██║██╔═╝  ╚██╗██╔╝   ██║   ██║ ██║██║ ██║██║    ╚═══██║
    {COLOR}██║ ╚╝ ██║█████╔╝██████╗ ╚███╔╝    ██║   ╚████╔╝╚████╔╝██████╗██████║
    {COLOR}╚═╝    ╚═╝╚════╝ ╚═════╝  ╚══╝     ╚═╝    ╚═══╝  ╚═══╝ ╚═════╝╚═════╝
                                    {Color.CCYAN2}© Copyright {YEAR}, {AUTHOR}. Version {VERSION}

    """


SMALL = f"""

    {COLOR}███╗   ███╗  ██████╗   ████████╗
    {COLOR}████╗ ████║  ██╔══██╗  ╚══██╔══╝
    {COLOR}██╔████╔██║  ██║  ██║     ██║   
    {COLOR}██║╚██╔╝██║  ██║  ██║     ██║   
    {COLOR}██║ ╚═╝ ██║  ██████╔╝     ██║   
    {COLOR}╚═╝     ╚═╝  ╚═════╝      ╚═╝   
    {Color.CCYAN2}© {YEAR}, {AUTHOR}. Version {VERSION}

    """



def __clearTerminal():
    sys = system()
    if sys == "Windows":
        os.system("cls")
    elif sys == "Darwin":
        os.system("clear")
    elif sys == "Linux":
        os.system("clear")



def showBanner():
    __clearTerminal()

    terminalWidth = get_terminal_size()[0]

    if terminalWidth >= 110:
        banner = XLARGE
    elif 100 <= terminalWidth < 110:
        banner = LARGE
    elif 74 <= terminalWidth < 100:
        banner = MEDIUM
    elif terminalWidth < 74:
        banner = SMALL

    for col in banner:
        print(col, end="")
        stdout.flush()
        sleep(0.001)
