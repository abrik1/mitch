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

user=getlogin()
hostname=gethostname()
totalramus=virtual_memory()[3]/1000000
totalram=virtual_memory().total/1000000
distro=name()
cpuarch=machine()
cpuname=get_cpu_info()['brand_raw']
kernver=release()
sh=getenv('SHELL')
de=getenv('DESKTOP_SESSION')
pathapk="/usr/bin/apk"
pathapt="/usr/bin/apt"
pathdnf="/usr/bin/dnf"
pathpacman="/usr/bin/pacman"
aptexists=isfile(pathapt)
pacmanexists=isfile(pathpacman)
dnfexists=isfile(pathdnf)

if pacmanexists==True:
    pcmd=check_output(['pacman' , '-Q']).decode('utf-8')
    pnum=len(pcmd.splitlines())
elif apkexists==True:    
    pcmd=check_output(['apk' , 'list' , '--installed']).decode('utf-8')
    pnum=len(pcmd.splitlines())    
elif aptexists==True:
    pcmd=check_output(['apt' , 'list' , '--installed']).decode('utf-8')
    pnum=len(pcmd.splitlines())
elif dnfexists==True:
    pcmd=check_output(['dnf' , 'list' , 'installed']).decode('utf-8')
    pnum=len(pcmd.splitlines())  

print('',' '+"\u001b[4m"+str(user)+str('@')+str(hostname)+'\u001b[0m')
print('',colorama.Fore.RED , " Distro:-" , colorama.Fore.RESET , distro + " " + cpuarch)
print('',colorama.Fore.GREEN , " CPU:-" , colorama.Fore.RESET, cpuname )
print('',colorama.Fore.BLUE , " Kernel:-" , colorama.Fore.RESET , kernver)
print('',colorama.Fore.YELLOW , " Packages:-" , colorama.Fore.RESET , pnum)
print('',colorama.Fore.CYAN , " Desktop Enviroment:-" , colorama.Fore.RESET , de)
print('',colorama.Fore.MAGENTA , " Memory:-" , colorama.Fore.RESET , str(int(totalramus))+str('MB') + str('/') + str(int(totalram))+str('MB '))
print('',colorama.Fore.WHITE , " Shell:-" , colorama.Fore.RESET , sh)

print()
print(colorama.Style.NORMAL,colorama.Fore.RED,'' , colorama.Fore.GREEN , '' , colorama.Fore.BLUE , '' , colorama.Fore.YELLOW , '' ,colorama.Fore.CYAN , '',colorama.Fore.MAGENTA , '' , colorama.Fore.WHITE , ' ')
print(colorama.Style.BRIGHT , colorama.Fore.RED,'' , colorama.Fore.GREEN , '' , colorama.Fore.BLUE , '' , colorama.Fore.YELLOW , '' ,colorama.Fore.CYAN , '',colorama.Fore.MAGENTA , '' , colorama.Fore.WHITE , ' ')
