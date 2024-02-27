import subprocess
import threading


# --- classes ---

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll

    def flush(self):
        print("HI")


# --- functions ---

def run():
    threading.Thread(target=test).start()


def test():
    print("Thread: start")

    p = subprocess.Popen("python extra.py rip_ddos 1.1.1.1".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:

        msg = p.stdout.readline().strip()  # read a line from theoutput
        if msg:
            print(msg)

    print("Thread: end")

