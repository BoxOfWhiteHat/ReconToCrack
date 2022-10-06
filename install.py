#!/usr/bin/python3

import os
import sys
import termcolor
from termcolor import cprint
def install():
    cprint("[*]Install Requirement ...","green",attrs=["bold"])
    print("")
    os.system("apt-get install hcxdumptool &&  pip3 install termcolor ")
    print("")
    if os.path.exists("/root/ReconToCrack/output"):
       print("ALL IS OK ..")
    if not os.path.exists("/root/ReconToCrack/output"):
       cprint("Folder output Created","green",attrs=["bold"])
       os.system("cd /root/ReconToCrack && mkdir output")
    if os.path.exists("/root/ReconToCrack/Result"):
       print("Result Folder Here")
    if not os.path.exists("/root/ReconToCrack/Result"):    
       os.system("cd /root/ReconToCrack && mkdir Result")
       cprint("Folder Result Created","green",attrs=["bold"])
    if not os.path.exists("/root/ReconToCrack/Kaonashi"):
       os.system("cd /root/ReconToCrack && mkdir Konashi")
       cprint("Folder Knoashi Created","green",attrs=["bold"])
       os.system("cd /root/ReconToCrack && chmod +x * && cp *.torrent /root/ReconToCrack/Konashi ")
install()
      
