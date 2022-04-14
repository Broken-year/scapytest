"""
scapytest
"""
import socket
import time

from scapy.all import *
from random import randint


from whois import whois
def main():
    # #百度域名信息
    # data= whois('www.baidu.com')
    # print(data)
    # print('---------')
    # #通过域名获得ip
    # ip = socket.gethostbyname('www.baidu.com')
    # print(ip)
    # print('----------')

    # #构建icmp扫描(方法一)
    # ip_id = randint(1,65535)
    # icmp_id = randint(1,65535)
    # icmp_seq = randint(1,65535)
    # packet = IP(dst='192.168.3.137',ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'rootkit'
    # result = sr1(packet,timeout=1,verbose=False)
    # if result:
    #     for rcv in result:
    #         scan_ip = rcv[IP].src
    #         print(scan_ip+'is alive')
    # else:
    #     print('is down')

    # #icmp扫描(方法二)
    # ans,uans = sr(IP(dst='192.168.3.137')/ICMP())
    # for snd,rcv in ans:
    #     print(rcv.sprintf("%IP.src% is alive now"))

    # #tcp扫描1（判断是否存活）
    # ans,uans = sr(IP(dst='192.168.3.137')/TCP(dport=80,flags='S'))
    # for snd,rcv in ans:
    #     print(rcv.sprintf("%IP.src% is up"))

    # #tcp扫描2
    # ip = '192.168.3.137'
    # dport = randint(1,65535)
    # packet = IP(dst=ip)/TCP(flags='A',dport=dport)
    # response = sr1(packet,timeout=1.0,verbose=0)
    # if response:
    #     #rst
    #     if int(response[TCP].flags)==4:
    #         time.sleep(0.5)
    #         print(ip+'is up')
    #     else:
    #         print(ip+'is down')

    # #udp扫描
    # ip = '192.168.3.137'
    # ans,uans = sr(IP(dst=ip)/UDP(dport=80))
    # for snd,rcv in ans:
    #     print(rcv.sprintf("%IP.src% is up"))

    #tcp全开放/半开放端口扫描
    """
    给目标发送syn,返回syn+ack,之后返回ack,成功连接tcp
    有可能会被主机日志记录下来,最后一次握手没用
    在目标返回syn+ack的时候就已经完成探测目的
    """
    ip = '192.168.3.137'
    port=3306
    packet = IP(dst=ip)/TCP(sport=12345,dport=port,flags='S')
    resp = sr1(packet,timeout=20)
    if(str(type(resp))=="<type 'NoneType'>"):
        print('port %s is closed'%(port))
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags==0x12):
            #flag是AR的时候是全开放 R的时候是半开放
            send_rst = sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="AR"),timeout=20)
            print("port %s is open"%(port))
        elif(resp.getlayer(TCP).flags==0x14):
            print("port %s is down"%(port))

    s = socket.socket()
    s.connect((ip,port))
    s.send('haha'.encode())
    banner = s.recv(1024)
    s.close()
    print('banner is {}'.format(banner))



    pass
if __name__ == '__main__':
    main()