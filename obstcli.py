#!/usr/bin/python

import  os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.10.191"
s_port=8888

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



