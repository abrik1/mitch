#Dependencies

from rich.console import Console
from rich.table import Table
from psutil import virtual_memory
from platform import machine, release
from distro import name,version
from cpuinfo import get_cpu_info
from os.path import isfile
from subprocess import check_output
from os import getlogin , getenv
from socket import gethostname
from pyfiglet import figlet_format

console = Console()
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
else:
    pnum = None

def ascii_art(distro):
    global asciiart , artprint
    asciiart = figlet_format(text=f"  {distro}")
    if distro=="Arch Linux" or distro=="Pop!_OS":
        artprint = f"[cyan] {asciiart} [/cyan]"
    elif distro=="Manjaro Linux" or distro=="Linux Mint" or distro=="Void Linux":
        artprint = f"[green] {asciiart} [/green]"
    elif distro=="EndeavourOS" or distro=="Gentoo":
        artprint = f"[magenta] {asciiart} [/magenta]"
    elif distro=="Ubuntu" or distro=="Debian":
        artprint = f"[red] {asciiart} [/red]"
    elif distro=="Alpine Linux" or distro=="ArcoLinux" or distro=="Fedora Linux":
        artprint = f"[blue] {asciiart} [/blue]"
    else:
        artprint = asciiart
        
ascii_art(distro)
console.print(artprint)

table = Table()

table.add_column("info:-")
table.add_column("output:-")
table.add_row(f"[red]distro:- [/red]" , f"{distro} {cpuarch}")
table.add_row("[green]cpu:- [/green]" , f"{cpuname}")
table.add_row("[blue]kernel:- [/blue]" , f"{kernver}")
table.add_row("[yellow]packages:- [/yellow]" , f"{pnum}")
table.add_row("[cyan]de:-[/cyan]" , f"{de}")
table.add_row("[magenta]memory:-[/magenta]" , f"{int(totalramus)}MB | {int(totalram)}MB")
table.add_row("[red]sh:-[/red]" , f"{sh}" , end_section=True)
table.add_row("[white]colors:-[/white]:-" , "[red] [/red][green] [/green][yellow] [/yellow][blue] [/blue][cyan] [/cyan][magenta] [/magenta]")


console.print(table)
