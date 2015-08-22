#!/usr/bin/env  python
#~*~coding:utf8~*~
# finame swtch_ip.py

import socket,os,sys
import ConfigParser
import time
from optparse import OptionParser

def init():
    global IPS
    global GATEWAYS
    config = ConfigParser.ConfigParser()
    dir = os.path.dirname(os.path.abspath(__file__))
    conf = dir + "/conf"
    filepath = "%s/ip.conf" %(conf)
    if not os.path.exists(filepath):
        raise "ERROR: ip.conf is not it!"
    config.read(filepath)
    IPS = config.get(options.type,"ip")
    GATEWAYS = config.get(options.type,"gateway")
    print "======[%s] Start get new options,please wait... ======" %(options.type)
    print "%s config file ip is %s,gateway is %s" %(options.type,IPS,GATEWAYS)

def getopts():
    MSG_USAGE='''python %s -t home''' % sys.argv[0]
    optParser=OptionParser(MSG_USAGE)
    optParser.add_option('-t',action='store',type='string',dest='type',default='work',help=u'type:work,home')
    (options,args)=optParser.parse_args()
    return options

def ipconfig():
    ipconfigfile = open('/etc/sysconfig/network-scripts/ifcfg-eth0','r')
    while True:
        ipconfiglines = ipconfigfile.readlines()
        if not ipconfiglines:
	    break
    	#ipconfigfile.close()
	if "IPADDR" in ipconfiglines[4] and "GATEWAY" in ipconfiglines[3]:
	    print "====== Change IP and GATEWAY, please wait... ======"
            temp = ipconfiglines[4].split('\"')
            a = temp[1]
            temp1 = ipconfiglines[3].split('\"')
            b = temp1[1]
            print "ifcfg-et0 config old IP is %s and old GATEWAY is %s" %(a,b)
            edit_file = os.system('sed -i "s/'+a+'/'+IPS+'/g;s/'+b+'/'+GATEWAYS+'/g" /etc/sysconfig/network-scripts/ifcfg-eth0')
            if edit_file == 0:
                print 'Edit ifcfg-eth0 ip and gateway is OK,restart network restart'
                restart_network = os.system('/etc/init.d/network restart')
		if restart_network == 0:
		    print "Network restart Succ!"
                else:
	            print "Network restart Fail!"
	    else:
                print 'Edit ifcfg-eth0 ip is ERROR'
	else:
	    print "no IP address and GATEWAY!!!"

if __name__ == '__main__':
    if len(sys.argv)<2 and sys.argv[1] != '-h' and sys.argv[1] != '--help':
        print '''Usage:  python %s -t work
        python %s -h|--help''' % (sys.argv[0],sys.argv[0])
        sys.exit(1)
    options = getopts()
    init()
    ipconfig()
