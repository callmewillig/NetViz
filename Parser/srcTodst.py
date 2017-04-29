"""
    Author: Matthew Willig
            Thomas Slota
            Nick Miller

    Network Visualization,
    NetFlow w/nfdump
"""

"""
Parser for text files

source(ip)-returns a list of destination IP addresses that interacted with a specific source IP address

destination(ip)-returns a list of source IP addresses that interacted with a specific destination IP address

sourcePort(port)-returns a list of source port numbers that interacted with a specific IP address

destinationPort(port)-returns a list of destination port numbers that interacted with a specific IP address
"""

#todo: Change the path to the proper directories


def source(ip):
    siLst = []
    with open("C:\\Users\Hikiba\Documents\School\Spring 2017\CSEC 462\Project\SipDip.txt") as f:
        line = f.readlines()[1:]
        for l in line:
            l = l.split()
            if l[0] == 'Summary:':
                break
            src = l[4].split(":")
            if src[0] == ip:
                dst = l[6].split(":")
                if siLst.__contains__(dst[0]):
                    continue
                siLst.append(dst[0])
        return siLst


def destination(ip):
    diLst = []
    with open("C:\\Users\Hikiba\Documents\School\Spring 2017\CSEC 462\Project\SipDip.txt") as f:
        line = f.readlines()[1:]
        for l in line:
            l = l.split()
            if l[0] == 'Summary:':
                break
            dst = l[6].split(":")
            if dst[0] == ip:
                src = l[4].split(":")
                if diLst.__contains__(src[0]):
                    continue
                diLst.append(src[0])
        return diLst


def sourcePort(ip):
    spLst = []
    with open("C:\\Users\Hikiba\Documents\School\Spring 2017\CSEC 462\Project\SipDip.txt") as f:
        line = f.readlines()[1:]
        for l in line:
            l = l.split()
            if l[0] == 'Summary:':
                break
            src = l[4].split(":")
            if src[0] == ip:
                dst = l[6].split(":")
                if spLst.__contains__(dst[1]):
                    continue
                spLst.append(dst[1])
        return spLst


def destinationPort(ip):
    dpLst = []
    with open("C:\\Users\Hikiba\Documents\School\Spring 2017\CSEC 462\Project\SipDip.txt") as f:
        line = f.readlines()[1:]
        for l in line:
            l = l.split()
            if l[0] == 'Summary:':
                break
            dst = l[6].split(":")
            if dst[0] == ip:
                src = l[4].split(":")
                if dpLst.__contains__(src[1]):
                    continue
                dpLst.append(src[1])
        return dpLst

def readFile():
    with open("C:\\Users\Hikiba\Documents\School\Spring 2017\CSEC 462\Project\SipDip.txt") as f:
        line = f.readlines()[1:]
        for l in line:
            print(l)


if __name__ == '__main__':
    print("Source to Destination IP method")
    print(source("172.16.15.200"))
    print(source("172.16.15.201"))
    print(source("172.16.5.1"))
    print(source("172.16.5.2"))
    print(source("172.16.5.3"))
    print(source("172.16.5.20"))

    print("\nDestination to Source IP method")
    print(destination("172.16.15.200"))
    print(destination("172.16.15.201"))
    print(destination("172.16.5.1"))
    print(destination("172.16.5.2"))
    print(destination("172.16.5.3"))
    print(destination("172.16.5.20"))


    print("\nSource to Destination port method")
    print(sourcePort("172.16.15.200"))
    print(sourcePort("172.16.15.201"))
    print(sourcePort("172.16.5.1"))
    print(sourcePort("172.16.5.2"))
    print(sourcePort("172.16.5.3"))
    print(sourcePort("172.16.5.20"))

    print("\nDestination to Source port method")
    print(destinationPort("172.16.15.200"))
    print(destinationPort("172.16.15.201"))
    print(destinationPort("172.16.5.1"))
    print(destinationPort("172.16.5.2"))
    print(destinationPort("172.16.5.3"))
    print(destinationPort("172.16.5.20"))

    # readFile()


