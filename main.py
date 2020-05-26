#!/bin/python3
from core.MacChanger import MACChanger
import argparse

print("""
    __  ______   ______    ________                               
   /  |/  /   | / ____/   / ____/ /_  ____ _____  ____ ____  _____
  / /|_/ / /| |/ /       / /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
 / /  / / ___ / /___    / /___/ / / / /_/ / / / / /_/ /  __/ /    
/_/  /_/_/  |_\____/____\____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
                  /_____/                      /____/             

[*] Author : Mahmoud S.ALi
[*] Facebook : https://www.facebook.com/mody.saber.96343405
[*] WhatsApp : 01117374028

""")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--interface", help="Interface for which you want to change MAC address", required=True)
    parser.add_argument("-m", "--newmac", help="New MAC address", required=True)
    
    args = parser.parse_args()
    iface = args.interface
    new_mac = args.newmac

    
    mc = MACChanger()
    print("[+] Current MAC is ", mc.getMAC(iface))
    res_mac = mc.Change_MAC(iface, new_mac)
    print("[+] updated MAC address is ", res_mac)

