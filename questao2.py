import os
import time
import sys

pid = os.fork()

if pid == 0:
    
    for i in range(6, 11):
        print(f"Filho: {i}")
        time.sleep(1)
    sys.exit(0)
else:
    os.wait()  
    for i in range(1, 6):
        print(f"Pai: {i}")
        time.sleep(1)