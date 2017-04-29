""""
interface.py
	This program will create a user interface with the capablilities to choose an
	address and gain various information based on that address.

libraries(sudo aot-get install...)
	python3-qt5(PyQt5)

Authors:
Tommy Slota
Mathew Willig
Nicholas Miller
"""
#-----imports-----
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
import os
from threading import Thread

####To Matt: COLLECT AND APPEND ADDRESS HERE FROM PARSER####
####There are static addresses bellow. Just Comment out####
adr = []


"""
-----IPWindow----
- Makes a second window with IP as title
"""
class IPWindow(QWidget):
    def __init__(self, address):
        super().__init__()
        self.IPWIN(address)
    
    #=====Creates the IPWindow=====
    #address-Button with address clicked
    def IPWIN(self, address):
        self.setFixedSize(400,300)
        self.setGeometry(265, 1, 0, 0)
        self.setWindowTitle(address) 
        self.show()	

"""
-----MainWindow-----
- Makes a small taskbar window
- Adds IP addresses from parser as clickable buttons
- Will open an "IP Window" if button is clicked(One at a time, but will be changed)
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
        global adr
        adr = ["172.16.177.2","255.255.255.255","1.1.1.1","111.111.111.111", "1.1.1.","13241234","1234123414","123412341234"] 
        self.setFixedSize(200, 300)
        
	
        #-----Makes Buttons and makes button a scrollable object-----
        buttons = {}
        size = 40       
        for count in range(0,len(adr)):
            buttons[count] = QPushButton(adr[count], self)
            buttons[count].setFixedSize(140,30)
#            buttons[count].move(0, 0+ (count * size))
            buttons[count].clicked[bool].connect(self.action)
            scrollLayout.addWidget(buttons[count])
        scroll.setWidget(scrollContent)
        
        #-----Sets the title window-----
        self.setGeometry(1, 1,0,0)
        self.setWindowTitle('IP Addresses')
        self.show()
        
    """
    -----Action--
    - When button is clicked, it opens a windows based on the button
    - Uses the IP address array
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
- MainWindow is executed and is also terminated when closed
"""
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
