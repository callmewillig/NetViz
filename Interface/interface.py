""""
interface.py

    This program will create a user interface with the capablilities to choose an
    address and gain various information based on that address.

libraries(sudo aot-get install...)

    python3-pyqt5(PyQt5)
    matplotlib

Authors

    Tommy Slota
    Mathew Willig
    Nicholas Miller
"""
#-----imports-----
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
import optparse
import os
from threading import Thread

#-----import graph/table programs----
from tablesANDgraphs import *
adr = []

"""
-----IPWindow----
=======================================================================
- Makes a second window with IP as title
=======================================================================
"""

class IPWindow(QWidget):
    def __init__(self, address):
        super().__init__()
        self.IPWIN(address)
    
    #=====Creates the IPWindow=====
    #address-Button with address clicked
    def IPWIN(self, address):
        #-----Set up window-----
        self.setFixedSize(360,110)
        self.setGeometry(265, 1, 0, 0)
        self.setWindowTitle(address)
        
        global ip
        ip = address
        #-----Labeling-----
        graphs = QLabel("Graphs",self)        
        graphs.move(55,10)
        
        tables = QLabel("Tables",self)
        tables.move(205,10)
        
        #-----Create Button----
        tuB = QPushButton("TCP vs UDP", self)
        tuB.setFixedSize(140,30)
        tuB.move(10,30)
        tuB.clicked[bool].connect(self.action)
        
        DestB = QPushButton("Destinations", self)
        DestB.setFixedSize(140,30)
        DestB.move(160,30)
        DestB.clicked[bool].connect(self.action)

        ProtoB = QPushButton("Top 10 Ports Used",self)
        ProtoB.setFixedSize(140,30)
        ProtoB.move(10,70)
        ProtoB.clicked[bool].connect(self.action)

        self.show()	

    """
    -----Action-----
    ==========================================================================
    - Pulls up specific table/graph depending on what button was clicked
    ==========================================================================
    """
    def action(self):
        global ip
        source = self.sender()
        if source.text() == "TCP vs UDP":
            tcpVudp(ip)
        elif source.text() == "Top 10 Ports Used":
            barGraph(ip)
        elif source.text() == "Destinations":
            setip(ip)
            self.destT = DestTable()
            self.destT.show()
        else:
            print(" ")

"""
-----MainWindow-----
===================================================================================
- Makes a small taskbar window
- Adds IP addresses from parser as clickable buttons
- Will open an "IP Window" if button is clicked(One at a time, but will be changed)
===================================================================================
""" 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #====Creates Main Taskbar====
    def initUI(self):
        
        #-----Initialize the taskbar layout-----
        box = QVBoxLayout(self)
        self.setLayout(box)
        scroll = QScrollArea(self)
        box.addWidget(scroll)
        scrollContent = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        
        #-----Make "adr" static array of addresses-----
        sys.path.insert(0, '../Parser/')
        from getIPs import getIPsStart
	
        global adr
        adr = getIPsStart() 
        self.setFixedSize(200, 300)
        
	
        #-----Makes Buttons and makes button a scrollable object-----
        buttons = {}
        size = 40       
        for count in range(0,len(adr)):
            buttons[count] = QPushButton(adr[count], self)
            buttons[count].setFixedSize(140,30)
            buttons[count].clicked[bool].connect(self.action)
            scrollLayout.addWidget(buttons[count])
        scroll.setWidget(scrollContent)
        
        #-----Sets the title window-----
        self.setGeometry(1, 1,0,0)
        self.setWindowTitle('IP Addresses')
        self.show()
        
    """
    -----Action-----
    =====================================================================
    - When button is clicked, it opens a windows based on the button
    - Uses the IP address array
    =====================================================================
    """
    def action(self):
        source = self.sender()
        global adr
        for i in range(0,len(adr)):
            if source.text() == adr[i]:
                self.IPwin = IPWindow(adr[i])
        self.IPwin.show()

"""
-----MAIN----
======================================================================
- MainWindow is executed and is also terminated when closed
======================================================================
"""
if __name__ == "__main__":
    parser = optparse.OptionParser(usage='''
        -s <start_time> time window start for filtering packets
		yyyy/MM/dd.hh:mm:ss
        -e <end_time> time window end for filtering packets
                yyyy/MM/dd.hh:mm:ss
        ''')

    parser.add_option('-s', '--start_time',
                      dest='start_time', action='store', type='string')
    parser.add_option('-e', '--end_time',
                      dest='end_time', action='store', type='string')

    (options, args) = parser.parse_args()

    if not options.start_time:
        if options.end_time:
            sys.exit("End time given but no start time was given.\n")
        else:
            os.system("nfdump -R ../nfcapd/ > ../Temp/SipDip.txt")
    else:
        if not options.end_time:
            thisstring = "nfdump -t " + options.start_time + " -R ../nfcapd/ > ../Temp/SipDip.txt"
            print(thisstring)
            os.system(thisstring)
        else:
            thisstring = "nfdump -t " + options.start_time + "-" + options.end_time + " -R ../nfcapd/ > ../Temp/SipDip.txt"
            print(thisstring)
            os.system(thisstring)


    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
