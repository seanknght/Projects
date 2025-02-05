from colorama import Fore, init, Style
from scapy.all import arping
import textwrap
import sys

#///////////////// ASCII BANNER ///////////////////

init(autoreset=True)

def ascii(color, text):
    colored_text = f"{color}{text}{Fore.RESET}"
    print(colored_text)

from colorama import Fore, init


asciiart = """


░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  v1.0.0      
                                                      
               SIMPLE ARP-SCANNER

"""

print(asciiart)

#///////////////// ASCII BANNER ///////////////////

def show_help():

    help_text = textwrap.dedent(

    """

    NUFF - Simple ARP Scanning Tool - Help
    Usage: python nuff.py [options]

    Options:

      -h, --help        Show this help message and exit
      -v, --version     Show the version of the NUFF tool
      -a, --about       Display information about the NUFF tool
    
      """)

    ascii(Fore.RED, help_text)

if '-h' in sys.argv or '--help' in sys.argv:
    show_help()
    sys.exit(0)

if '-v' in sys.argv or '--version' in sys.argv:
    ascii(Fore.RED, "NUFF - Version 1.0.0")
    sys.exit(0)

if '-a' in sys.argv or '--about' in sys.argv:
    ascii(Fore.RED, "NUFF is simple arp-scanner made by Sean Knight.")
    sys.exit(0)

def nuff():

    arping("192.168.0.1/24")

if __name__ == '__main__':

    nuff()



