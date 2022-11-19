#Dependencies

import colorama
from psutil import virtual_memory
from platform import machine, release , version
from cpuinfo import get_cpu_info
from os.path import isfile
from subprocess import check_output
from os import getlogin 
from socket import gethostname
from pyfiglet import figlet_format

colorama.init()

user = getlogin()
hostname = gethostname()
totalramus = virtual_memory()[3]/1000000
totalram = virtual_memory().total/1000000
cpuarch = machine()
cpuname = get_cpu_info()['brand_raw']
release = release()
kernver = version()
packagecmd=check_output(["winget" , "list"]).decode('UTF-8')

packagenum=len(packagecmd.splitlines())
packagenum=packagenum-2

asciiart=figlet_format(text=f"Windows {release}")
print(f"{colorama.Fore.CYAN} {asciiart} {colorama.Fore.RESET}")

print('',' '+"\u001b[4m"+str(user)+str('@')+str(hostname)+'\u001b[0m')
print('',colorama.Fore.RED , " Windows:-" , colorama.Fore.RESET , f"Windows {release}" + " " + cpuarch)
print('',colorama.Fore.GREEN , " CPU:-" , colorama.Fore.RESET, cpuname )
print('',colorama.Fore.BLUE , " Kernel:-" , colorama.Fore.RESET , f"{kernver}")
print('',colorama.Fore.YELLOW , " Packages:-" , colorama.Fore.RESET , f"{packagenum}")
print('',colorama.Fore.CYAN , " Desktop Enviroment:-" , colorama.Fore.RESET , "Aero")
print('',colorama.Fore.MAGENTA , " Memory:-" , colorama.Fore.RESET , str(int(totalramus))+str('MB') + str('/') + str(int(totalram))+str('MB '))
print('',colorama.Fore.WHITE , " Shell:-" , colorama.Fore.RESET , "psh")

print()
print(colorama.Style.NORMAL,colorama.Fore.RED,'' , colorama.Fore.GREEN , '' , colorama.Fore.BLUE , '' , colorama.Fore.YELLOW , '' ,colorama.Fore.CYAN , '',colorama.Fore.MAGENTA , '' , colorama.Fore.WHITE , ' ')
print(colorama.Style.BRIGHT , colorama.Fore.RED,'' , colorama.Fore.GREEN , '' , colorama.Fore.BLUE , '' , colorama.Fore.YELLOW , '' ,colorama.Fore.CYAN , '',colorama.Fore.MAGENTA , '' , colorama.Fore.WHITE , ' ')
