#!/usr/bin/python
"""
    Author: Matthew Willig
            Thomas Slota
            Nick Miller
            
    Network Visualization,
    NetFlow w/nfdump
"""

"""
syscall for nfdump to create file for parsing

./nfdump -R ./"file"  dstip
./nfdump -R ./nfcapd/  > /nfdumpout/SipDip.txt
/visProj/nfcapd/nfcapd.120398712894
/visProj/nfdumpout/SipDip.txt



NEED TO ASK FOR START AND END DATES SO THAT NFDUMP CAN DO ONLY A CERTAIN TIME PERIOD.
Dpacket 
Skapey

"""

import os
import socket as sock
"""
    return array of ip's within the file
"""

def getIPsStart():
    os.system("nfdump -R ../nfcapd/ > ../Temp/SipDip.txt")
    #os.system("nfdump -R ../nfcapd/ > ../nfdumpout/SipDip.txt")
    with open("../Temp/SipDip.txt") as f:
        content = f.readlines()
        
    del content[0]

    temp = []
    for data in content:	
        temp.append(data.split())

    ips = []

    for line in temp:
    #    print(line)
        if line[0] == "Summary:":
            break
        else:
            ips.append(str(line[4]))
            ips.append(str(line[6]))

    ip2 = []

    for ip in ips:
        ip2.append(ip.split(':'))

    ip3 = []

    unique_ips = [list(x) for x in set(tuple(x) for x in ip2)]


    for ip in unique_ips:
        ip3.append(ip[0])    
    ip3 = list(set(ip3))

    
    ip3.sort(key=lambda s: list(map(int, s.split('.'))))
    #print(ip3)

    return ip3


"""
def getPorts():
    with open("../nfdumpout/SipDip.txt") as f:
        content = f.readlines()
        
    del content[0]

    temp = []
    for data in content:	
        temp.append(data.split())

    ips = []

    for line in temp:
    #    print(line)
        if line[0] == "Summary:":
            break
        else:
            ips.append(str(line[4]))
            ips.append(str(line[6]))

    ip2 = []

    for ip in ips:
        ip2.append(ip.split(':'))
    unique_ips = [list(x) for x in set(tuple(x) for x in ip2)]

    ports = []
    for ip in unique_ips:
        ports.append(ip[1])    
    ports = list(set(ports))

    
    ports.sort(key=lambda s: list(map(int, s.split('.'))))
   # print(ports)
    return ports

def getIPandPorts():
    with open("../nfdumpout/SipDip.txt") as f:
        content = f.readlines()
        
    del content[0]

    temp = []
    for data in content:	
        temp.append(data.split())

    ips = []

    for line in temp:
    #    print(line)
        if line[0] == "Summary:":
            break
        else:
            ips.append(str(line[4]))
            ips.append(str(line[6]))


    combinedip = []
    
    for ips2 in range(len(ips)/2):
        combinedip.append([ips[ips2], ips[ips2+1]])



    unique_ips = []

    unique_ips = [list(x) for x in set(tuple(x) for x in combinedip)]
    #print(unique_ips)
    return unique_ips
"""


