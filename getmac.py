from core.MacChanger import MACChanger

iface = "eth0"

mc = MACChanger()
print(mc.getMAC(iface))
