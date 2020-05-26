import subprocess
import re


class MACChanger:
    def __init__(self):
        self.MAC = ""

    def getIP(self, iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

        pattern = r'inet\s[^a-z]*[.]1[^a-z]*[.]1[^a-z]'

        cmd_result = output.stdout.decode('utf-8')
        regex = re.compile(pattern)
        ans = regex.search(cmd_result)

        found_ip = ans.group().split(" ")[1]
        return found_ip

    def getMAC(self, iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)
        pattern = r'ether\s{1}[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        cmd_result = output.stdout.decode('utf-8')
        regex = re.compile(pattern)
        ans = regex.search(cmd_result)
        current_mac = ans.group().split(" ")[1]
        return current_mac

    def Change_MAC(self, iface, newMAC):
        """ Changes the MAC address on Linux
        
        Arguments:
            iface {string} -- Name of the interface
            newMAC {string} -- New MAC address that you want to set up
        
        Returns:
            updated_MAC --  Updated MAC address
                    """        
        print("[+] Changing MAC for ", iface, " to ", newMAC)
        self.MAC = self.getMAC(iface=iface)
        print("[+] Shutting down interface ", iface)
        output = subprocess.run(["ifconfig", iface, "down"], shell=False, capture_output=True)
        err = output.stderr.decode('utf-8')
        if err != "":
            print(err)
        print("[+] Changing MAC address to ", newMAC)
        output = subprocess.run(["ifconfig", iface, "hw", "ether", newMAC], shell=False, capture_output=True)
        err = output.stderr.decode('utf-8')
        if err != "":
            print(err)

        output = subprocess.run(["ifconfig", iface, "up"], shell=False, capture_output=True)
        err = output.stderr.decode('utf-8')
        if err != "":
            print(err)
        return self.getMAC(iface)
