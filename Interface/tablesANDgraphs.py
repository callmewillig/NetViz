import matplotlib.pyplot as plt
from PyQt5 import *
from PyQt5.QtWidgets import *
import numpy as np
import sys
sys.path.insert(0, '../Parser/')
from info import tcpudp, portCount

class DestTable(QWidget):
    def __init__(self):
        super().__init__()
        self.table()
    
    def table(self):
        self.setWindowTitle("Sent To...")
        adr = ["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4","5.5.5.5","255.255.255.255"]

        #-----Create Table Object
        table = QTableWidget()
        

        #-----Set Row and Columns-----
        table.setRowCount(len(adr))
        table.setColumnCount(1)
        table.setHorizontalHeaderLabels(["Destinations"])
        table.horizontalHeader().setStretchLastSection(True)

        #-----Set Addresses in table-----
        for count in range(0,len(adr)):
            table.setItem(count, 0 , QTableWidgetItem(adr[count]))
        table.move(0,0)
        
        #-----Edit Table Layout-----
        self.layout = QVBoxLayout()
        self.layout.addWidget(table)
        self.setLayout(self.layout)

        self.setGeometry(400,400,185,300)
        self.show()

def tcpVudp(ip):
    array = tcpudp(ip)
    sizes = []
    labels= []
    if array[0] != 0:
        labels.append("TCP")
        sizes.append(array[0])
    if array[1] != 0:
        labels.append("UDP")
        sizes.append(array[1])
    if array[2] != 0:
        labels.append("OTHER")
        sizes.append(array[2])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=["blue","cyan","magenta"], labels=labels, autopct='%30.1f%%',
        shadow=True, startangle=180)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def barGraph(ip):
    ports = portCount(ip)
    performance = []
    fig, ax = plt.subplots()
    labels = []
    for key in ports:
        labels.append(key)
    
    y_pos = 3 + 10 * np.arange(len(labels))
    
    for i in range(0,len(ports)):
        performance.append(ports[labels[i]])

    ax.barh(y_pos, performance, align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('')
    ax.set_title('F.B.G.M.')

    plt.show()
