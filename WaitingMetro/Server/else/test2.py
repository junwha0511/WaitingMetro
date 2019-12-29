from current import Current
import threading
import time

class want(threading.Thread):
    def run(self): 
        def wanted():
            print("0.당고개")
            time.sleep(5)

a = Current()
b = want()

a.start()
b.start()
