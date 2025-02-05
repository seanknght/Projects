#SEAN KNIGHT
#FEB 3, 2025

#NUFF IS A NETWORK MAPPING TOOL.

from colorama import Fore, init, Style
import sys
from scapy.all import *
from scapy.all import arping
import textwrap
import ipaddress


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
                                                      
             NUFF NETWORK SCANNER

"""

print(asciiart)

#///////////////// ASCII BANNER ///////////////////

def show_help():
    help_text = textwrap.dedent("""
    NUFF Network scanning Tool - Help
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
    ascii(Fore.RED, "NUFF Tool Version 1.0")
    sys.exit(0)

if '-a' in sys.argv or '--about' in sys.argv:
    ascii(Fore.RED, "NUFF is s Network scanning tool to be evolved into a tool as powerful as nmap. Created by SEAN KNIGHT.")
    sys.exit(0)

def nuff(target):

    try:
        
        try:
            
            network = ipaddress.ip_network(target, strict= False)

        except:

            print("Invalid IP address or CIDR range.")
            return

        
        print(f"Scanning {target}")
        arping(str(network))

    except:

        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP Network Scanner")
    parser.add_argument("target")
    args = parser.parse_args()
    nuff(args.target)

