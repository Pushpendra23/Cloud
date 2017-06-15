#!/usr/bin/python

import  os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s_ip="192.168.10.191"
#s_ip="192.168.43.48"
s_ip="192.168.122.1"
s_port=8888

#Inform the server and providing with the ip of client to initiate the process of showing menu
s.sendto("ok",(s_ip,s_port))

#Storing received menu from server
menu=s.recvfrom(1000)
print menu[0]

#option stores the suitable option choosen by the user as per the requirement
option=raw_input("\nEnter your Choice : ")

#Confirming the input  is the desired one only
if option == '1' or option == '2':
	#Sending choice to server
	s.sendto(option,(s_ip,s_port))
else:
	print "Wrong choice ... Be Wise ... Thank You ..."
	execfile('trig.py')

#msg receives the message to be displayed to client to be interactive
msg=s.recvfrom(100)
print msg[0]
"""
drive_name=raw_input("enter  storage  drive  name  :  ")
drive_size=raw_input("enter  drive  size MB :  ")
s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))

res=s.recvfrom(4)

if   res[0]  ==  "done" :
	os.system('mkdir   /media/'+drive_name)
	os.system('mount  '+s_ip+':/mnt/'+drive_name+'   /media/'+drive_name)

else  :
	print   "No response  from  storage  cloud "
"""



