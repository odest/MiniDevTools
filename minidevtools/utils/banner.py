import os
import random
import dataclasses

from time import sleep
from sys import stdout
from platform import system

from .terminalsize import get_terminal_size
from .config import AUTHOR, VERSION


@dataclasses.dataclass
class Color:
    """A class containing color codes for terminal text."""

    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    CGREEN2 = "\033[32m"
    CYELLOW2 = "\033[93m"
    CPURPLE2 = "\033[0;35m"
    CCYAN2 = "\033[36m"
    ENDC = "\033[0m"


COLOR = random.choice(
    [
        Color.CRED2,
        Color.CBLUE2,
        Color.CGREEN2,
        Color.CYELLOW2,
        Color.CPURPLE2,
        Color.CCYAN2,
        Color.ENDC,
    ]
)

XLARGE = f"""

    {COLOR}███╗   ███╗ ██╗ ███╗   ██╗ ██╗ ██████╗  ███████╗ ██╗   ██╗ ████████╗  ██████╗   ██████╗  ██╗      ███████╗
    {COLOR}████╗ ████║ ██║ ████╗  ██║ ██║ ██╔══██╗ ██╔════╝ ██║   ██║ ╚══██╔══╝ ██╔═══██╗ ██╔═══██╗ ██║      ██╔════╝
    {COLOR}██╔████╔██║ ██║ ██╔██╗ ██║ ██║ ██║  ██║ █████╗   ██║   ██║    ██║    ██║   ██║ ██║   ██║ ██║      ███████╗
    {COLOR}██║╚██╔╝██║ ██║ ██║╚██╗██║ ██║ ██║  ██║ ██╔══╝   ╚██╗ ██╔╝    ██║    ██║   ██║ ██║   ██║ ██║      ╚════██║
    {COLOR}██║ ╚═╝ ██║ ██║ ██║ ╚████║ ██║ ██████╔╝ ███████╗  ╚████╔╝     ██║    ╚██████╔╝ ╚██████╔╝ ███████╗ ███████║
    {COLOR}╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝ ╚═════╝  ╚══════╝   ╚═══╝      ╚═╝     ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝
                                                                                {Color.CCYAN2}developed by {AUTHOR} | v{VERSION}

    """


LARGE = f"""

    {COLOR}███╗   ███╗██╗███╗   ██╗██╗██████╗ ███████╗██╗   ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
    {COLOR}████╗ ████║██║████╗  ██║██║██╔══██╗██╔════╝██║   ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    {COLOR}██╔████╔██║██║██╔██╗ ██║██║██║  ██║█████╗  ██║   ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
    {COLOR}██║╚██╔╝██║██║██║╚██╗██║██║██║  ██║██╔══╝  ╚██╗ ██╔╝   ██║   ██║   ██║██║   ██║██║     ╚════██║
    {COLOR}██║ ╚═╝ ██║██║██║ ╚████║██║██████╔╝███████╗ ╚████╔╝    ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    {COLOR}╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═════╝ ╚══════╝  ╚═══╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                    {Color.CCYAN2}developed by {AUTHOR} | v{VERSION}
    
    """


MEDIUM = f"""

    {COLOR}███╗  ███╗█████╗ ██████╗██╗  ██╗████████╗ ████╗  ████╗ ██╗    ██████╗
    {COLOR}████╗████║██╔═██╗██╔═══╝██║  ██║╚══██╔══╝██╔═██╗██╔═██╗██║    ██╔═══╝
    {COLOR}██╔███╔██║██║ ██║████╗  ██║  ██║   ██║   ██║ ██║██║ ██║██║    ██████╗
    {COLOR}██║╚█╔╝██║██║ ██║██╔═╝  ╚██╗██╔╝   ██║   ██║ ██║██║ ██║██║    ╚═══██║
    {COLOR}██║ ╚╝ ██║█████╔╝██████╗ ╚███╔╝    ██║   ╚████╔╝╚████╔╝██████╗██████║
    {COLOR}╚═╝    ╚═╝╚════╝ ╚═════╝  ╚══╝     ╚═╝    ╚═══╝  ╚═══╝ ╚═════╝╚═════╝
                                        {Color.CCYAN2}developed by {AUTHOR} | v{VERSION}

    """


SMALL = f"""

    {COLOR}███╗   ███╗  ██████╗   ████████╗
    {COLOR}████╗ ████║  ██╔══██╗  ╚══██╔══╝
    {COLOR}██╔████╔██║  ██║  ██║     ██║   
    {COLOR}██║╚██╔╝██║  ██║  ██║     ██║   
    {COLOR}██║ ╚═╝ ██║  ██████╔╝     ██║   
    {COLOR}╚═╝     ╚═╝  ╚═════╝      ╚═╝   
    {Color.CCYAN2}developed by {AUTHOR} | v{VERSION}

    """


def __clear_terminal():
    sys = system()
    if sys == "Windows":
        os.system("cls")
    elif sys == "Darwin":
        os.system("clear")
    elif sys == "Linux":
        os.system("clear")


def show_banner():
    __clear_terminal()

    terminal_width = get_terminal_size()[0]
    banner = SMALL

    if terminal_width >= 110:
        banner = XLARGE
    elif 100 <= terminal_width < 110:
        banner = LARGE
    elif 74 <= terminal_width < 100:
        banner = MEDIUM
    elif terminal_width < 74:
        banner = SMALL

    for col in banner:
        print(col, end="")
        stdout.flush()
        sleep(0.001)
