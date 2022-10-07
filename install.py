#!/usr/bin/python3

#BoxOfWhiteHat

import os
import sys
import termcolor
from termcolor import cprint , colored
def install():
    kali=("1")
    Cemaxecuter=("2")

    cprint(" [1] kali linux / [2] DragonOS Focal By Cemaxecuter","green",attrs=["bold"])
    print("")
    OsInstaller=input(termcolor.colored("[*]System :"  ,"white",attrs=["bold"]))
    if OsInstaller == kali:   
       cprint("[*]Install Kali  Requirement ...","green",attrs=["bold"])
       print("")
       os.system("apt-get install hcxdumptool  hashcat &&  pip3 install termcolor ")
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
          os.system("cd /root/ReconToCrack && mkdir Kaonashi && cd Kaonashi && mkdir wordlists")
          cprint("Folder Knoashi Created","green",attrs=["bold"])
          os.system("cd /root/ReconToCrack && chmod +x * && mv *.torrent /root/ReconToCrack/Kaonashi/wordlists ")
          os.system("rm /usr/src/ReconToCrack/DragonWpa2ToHashcat  && rm /usr/src/ReconToCrack/DragonMaster")
    if OsInstaller == Cemaxecuter:  
          cprint("[*]Install DragonOs Requirement ...","green",attrs=["bold"])
          print("")
          os.system("sudo  apt-get remove hcxdumptool  hashcat &&  pip3 install termcolor ")
          os.system("sudo git clone  https://github.com/ZerBea/hcxtools   && cd hcxtools && sudo make -j4  && sudo make install && sudo ldconfig ")
          os.system("cd /usr/src/ReconToCrack/ && sudo git clone https://github.com/ZerBea/hcxdumptool && cd  hcxdumptool &&  sudo make -j4  && sudo make install && sudo ldconfig")
          os.system("cd  /usr/src/ReconToCrack/hcxdumptool   && sudo cp  hcxdumptool  hcxpioff  /usr/src/ReconToCrack/hcxtools ")
          print("")
          if os.path.exists("/usr/src/ReconToCrack/output"):
             print("ALL IS OK ..")
          if not os.path.exists("/usr/src/ReconToCrack/output"):
             cprint("Folder output Created","green",attrs=["bold"])
             os.system("cd /usr/src/ReconToCrack && mkdir output")
          if os.path.exists("/usr/src/ReconToCrack/Result"):
             print("Result Folder Here")
          if not os.path.exists("/usr/src/ReconToCrack/Result"):    
             os.system("cd /usr/src/ReconToCrack && mkdir Result")
             cprint("Folder Result Created","green",attrs=["bold"])
          if not os.path.exists("/usr/src/ReconToCrack/Kaonashi"):
             os.system("cd /usr/src/ReconToCrack && mkdir Kaonashi && cd Kaonashi && mkdir wordlists ")
             cprint("Folder Knoashi Created","green",attrs=["bold"])
             os.system("cd /usr/src/ReconToCrack && chmod +x * && mv *.torrent /usr/src/ReconToCrack/Kaonashi/wordlists  ")
             os.system("sudo rm /usr/src/ReconToCrack/Wpa2ToHashcat  && sudo rm /usr/src/ReconToCrack/Master")
             os.system("cd /usr/src/ReconToCrack  && sudo wget https://github.com/hashcat/hashcat/releases/download/v6.2.5/hashcat-6.2.5.7z ")  
             print("")
             cprint("extract hashcat-6.2.5.7z and rename to hashcat ","green",attrs=["bold"])
             
    else:
          print("")
          cprint(" Only Support  kali linux and   DragonOS Focal ","green",attrs=["bold"])
          
install()
      
