#Dependencies

import colorama
from psutil import virtual_memory
from platform import machine, release
from distro import name,version
from cpuinfo import get_cpu_info
from os.path import isfile
from subprocess import check_output
from os import getlogin , getenv
from socket import gethostname
from pyfiglet import figlet_format

user = getlogin()
hostname = gethostname()
totalramus = virtual_memory()[3]/1000000
totalram = virtual_memory().total/1000000
distro = name()
cpuarch = machine()
cpuname = get_cpu_info()['brand_raw']
kernver = release()
sh = getenv('SHELL')
de = getenv('DESKTOP_SESSION')
pathapk = "/usr/bin/apk"
pathapt = "/usr/bin/apt"
pathdnf = "/usr/bin/dnf"
pathpacman = "/usr/bin/pacman"
aptexists = isfile(pathapt)
apkexists = isfile(pathapk)
pacmanexists = isfile(pathpacman)
dnfexists = isfile(pathdnf)

if pacmanexists == True:
    pcmd = check_output(['pacman' , '-Q']).decode('utf-8')
    pnum = len(pcmd.splitlines())
elif apkexists == True:    
    pcmd = check_output(['apk' , 'list' , '--installed']).decode('utf-8')
    pnum = len(pcmd.splitlines())    
elif aptexists == True:
    pcmd = check_output(['apt' , 'list' , '--installed']).decode('utf-8')
    pnum = len(pcmd.splitlines())
elif dnfexists == True:
    pcmd = check_output(['dnf' , 'list' , 'installed']).decode('utf-8')
    pnum = len(pcmd.splitlines())  

def ascii_art(distro):
    global asciiart , artprint
    asciiart = figlet_format(text=f"  {distro}")
    if distro=="Arch Linux" or distro=="Pop!_OS":
        artprint = f"{colorama.Fore.CYAN} {asciiart} {colorama.Fore.RESET}"
    elif distro=="Manjaro Linux" or distro=="Linux Mint" or distro=="Void Linux":
        artprint = f"{colorama.Fore.GREEN} {asciiart} {colorama.Fore.RESET}"
    elif distro=="EndeavourOS" or distro=="Gentoo":
        artprint = f"{colorama.Fore.MAGENTA} {asciiart} {colorama.Fore.RESET}"
    elif distro=="Ubuntu" or distro=="Debian":
        artprint = f"{colorama.Fore.RED} {asciiart} {colorama.Fore.RESET}"
    elif distro=="Alpine Linux" or distro=="Arco Linux" or distro=="Fedora Linux":
        artprint = f"{colorama.Fore.BLUE} {asciiart} {colorama.Fore.RESET}"
ascii_art(distro)
print(artprint)

print('',' '+"\u001b[4m"+str(user)+str('@')+str(hostname)+'\u001b[0m')
print(f"{colorama.Fore.RED}   Distro:-  {colorama.Fore.RESET} {distro} {cpuarch}")
print(f"{colorama.Fore.GREEN}   CPU:- {colorama.Fore.RESET} {cpuname}")
print(f"{colorama.Fore.BLUE}   Kernel:- {colorama.Fore.RESET} {kernver}")
print(f"{colorama.Fore.YELLOW}   Packages:- {colorama.Fore.RESET} {pnum}")
print(f"{colorama.Fore.CYAN}   Desktop Enviroment:- {colorama.Fore.RESET} {de}")
print(f" {colorama.Fore.MAGENTA}  Memory:- {colorama.Fore.RESET} {int(totalramus)}MB/{int(totalram)}MB")
print(f" {colorama.Fore.WHITE}  Shell:- {colorama.Fore.RESET} {sh}")

print()
print(f"{colorama.Style.NORMAL}{colorama.Fore.RED}   {colorama.Fore.GREEN} {colorama.Fore.BLUE} {colorama.Fore.YELLOW} {colorama.Fore.CYAN} {colorama.Fore.MAGENTA} {colorama.Fore.WHITE} {colorama.Fore.RESET}")
print(f"{colorama.Style.BRIGHT}{colorama.Fore.RED}   {colorama.Fore.GREEN} {colorama.Fore.BLUE} {colorama.Fore.YELLOW} {colorama.Fore.CYAN} {colorama.Fore.MAGENTA} {colorama.Fore.WHITE} {colorama.Fore.RESET}")
