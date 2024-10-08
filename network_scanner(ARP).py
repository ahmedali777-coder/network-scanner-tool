
from scapy.all import ARP,Ether ,srp
import time
#ip's range network to scan
ip="192.168.1.1/24"
count=0
ip=[]
mac=[]

#prepare arp protocol with range of network ips and broadcast mac
arp_req= ARP(pdst=ip)
broadcast= Ether(dst="ff:ff:ff:ff:ff:ff")
arp_broadcast= broadcast/arp_req

#loop more than 1 as devices not always reply they may busy 
while count < 4 :
    #sending arp requests by srp 
    result= srp(arp_broadcast,timeout=0,verbose=True)[0]
    if len(result)== 0:
        continue
    for i in result:
        ip.append(i[1].psrc)
        mac.append(i[1].hwsrc)
      
    count+=1
    time.sleep(10)
#remove duplicate ips & macs
updated_ip=list(set(ip))
updated_mac=list(set(mac))
print("\n")
print("IP Addresses ")
print("________________________________")
print("\n")
for j in updated_ip :
    
    print(j)
print("\n")

print("MAC Addresses with respectively")
print("________________________________")
print("\n")
for k in updated_mac :
    
    print(k)
print("\n")
