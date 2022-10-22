#Dependencies

import colorama
from psutil import virtual_memory
from platform import machine, release
from distro import name,version
from cpuinfo import get_cpu_info
from os.path import isfile
from subprocess import check_output

totalramus=virtual_memory()[3]/1000000
totalram=virtual_memory().total/1000000
hostfile=open('/proc/sys/kernel/hostname')
hostname=hostfile.read()
distro=name()
cpuarch=machine()
cpuname=get_cpu_info()['brand_raw']
kernver=release()
pathapt="/usr/bin/apt"
pathdnf="/usr/bin/dnf"
pathpacman="/usr/bin/pacman"
aptexists=isfile(pathapt)
pacmanexists=isfile(pathpacman)
dnfexists=isfile(pathdnf)

if pacmanexists==True:
    pcmd=check_output(['pacman' , '-Q']).decode('utf-8')
    pnum=len(pcmd.splitlines())
elif aptexists==True:
    pcmd=check_output(['pacman' , '-Q']).decode('utf-8')
    pnum=len(pcmd.splitlines())
elif dnfexists==True:
    pcmd=check_output(['dnf' , 'list' , 'installed']).decode('utf-8')
    pnum=len(pcmd.splitlines())

print(colorama.Fore.RED , " Distro:-" , colorama.Fore.WHITE , distro + " " + cpuarch)
print(colorama.Fore.GREEN , " CPU:-" , colorama.Fore.WHITE, cpuname )
print(colorama.Fore.BLUE , " Kernel:-" , colorama.Fore.WHITE , kernver)
print(colorama.Fore.YELLOW , " Packages:-" , colorama.Fore.WHITE , pnum )
print(colorama.Fore.MAGENTA , " Memory:-" , colorama.Fore.WHITE , str(int(totalramus))+str('MB') + str('/') + str(int(totalram))+str('MB '))

print()
print(colorama.Fore.RED,'' , colorama.Fore.GREEN , '' , colorama.Fore.BLUE , '' , colorama.Fore.YELLOW , '' ,colorama.Fore.CYAN , '',colorama.Fore.MAGENTA , '' , colorama.Fore.WHITE , '')
