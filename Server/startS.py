#!/usr/bin/python


#Python script to automate STAAS cloud services

#Importing required modules
import  os,commands,sys,socket,time

#Forming socket and binding it 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))

print "Waiting for the client to trigger the process..."

#get_info notice the triggering and store the detail of client 
get_info=s.recvfrom(2)

#menu contains the message to be given to user to select from
menu="""The era of cloud is coming...
                                     Congratulation on your early start to the new era
Press 1 if your Storage requirement is in Mb
Press 2 if your Storage requirement is in Gb
"""

#Printing the menu on client screen
s.sendto(menu,get_info[1])

#receiving choice of client in choice 
choice=s.recvfrom(1)

#print "choice received"

if choice[0] == '1':
	#msg sends the message according to choice to remain interactive
	msg="It's really easy to maintain small storage ..."
	s.sendto(msg,get_info[1])
	execfile("fix_storage_allocation.py")
elif choice[0] == '2':
	#msg sends the message according to choice to remain interactive
	msg="Big idea need Big space"
	s.sendto(msg,get_info[1])
	execfile('thin_pool_storage_allocation.py')
else:
	print  "Something went wrong"







