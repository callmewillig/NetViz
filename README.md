#Authors:
#    Mathew Willig
#    Thomas Slota
#    Nicholas Miller

#NetvizProject:
#   How it works:
#       -The NetvizProject is a Netflow Visualizer that allows a user to collect and display Netflow     
#   data using different charts/graphs and lists.
#       - Written and parsed in Python 3.04.
#       - Graphs and charts created using PyQt5/metplotlib
#       - Use of nfdump to create a text file which is used by the parsers.
#       - Used and Tested on Linux Debian

#Dependencies
#  - PyQt5
#  - metplotlib
#  - Python 3.04

#Prerequisits
#  - nfdump takes the information and gives it to SipDip.txt
#  - SipDip.txt is then output to the /temp/ folder.

#To Run:
#   In the terminal
#       - python3 interface.py
#       - This will bring up an interface with a populated list of IP addresses connected to buttons.
#       - When a user clicks the IP address they would like to view a window pops up with 
#             buttons and  various information. Clicking on any of these buttons will show the 
# requested  information in different ways.
     

