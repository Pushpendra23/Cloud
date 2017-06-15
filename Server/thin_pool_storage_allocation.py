#!/usr/bin/python

import  os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8888))


while True:
	print "client had choosen the thin LVM"

	#  data  will recv  drive  name 
	data=s.recvfrom(20)
	d_name=data[0]
	#  data1  will recv  drive  size 
	data1=s.recvfrom(10)
	d_size=data1[0]
	#  here  client  address will be stored  
	cliaddr=data1[1][0]
	# creating thin LVM pool by the name of  client  drive  
	os.system('lvcreate  -V'+d_size+'G --name '+d_name+' --thin  volgrp/pool')
	# now time for  format  client  drive with  ext4 /  xfs  
	os.system('mkfs.xfs   /dev/volgrp/'+d_name)
	# now creating  mount point  
	os.system('mkdir   /mnt/'+d_name)
	# now mounting   drive locallly  
	os.system('mount  /dev/volgrp/'+d_name+'  /mnt/'+d_name)
	#  Now  time  for  NFS server  configuration  
	#os.system('yum  install   nfs-utils  -y')
	#making  entry  in  Nfs export  file 
	entry="/mnt/"+d_name+"  "+cliaddr+"(rw,no_root_squash)"
	#  appending  this  var  to  /etc/exports  file 
	f=open('/etc/exports','a')
	f.write(entry)
	f.write("\n")
	f.close()
	# finally  starting  nfs  service  and service  persistant 
	#os.system('systemctl   restart  nfs-server')
	#os.system('systemctl   enable  nfs-server')
	check=os.system('exportfs  -r')
	if  check  ==    0 :
		s.sendto("done",data1[1])
		print "data sent drive will be mounted"
	else :
		print   "plz  check  your  code  "
