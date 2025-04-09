import os
import time
import sys

pid = os.fork()

if pid == 0:
    # Processo filho
    for i in range(5):
        print(f"Filho fala: {i + 1}")
        time.sleep(1)
    sys.exit(0)
else:
    # Processo pai
    os.wait()  
    for i in range(5):
        print(f"Pai fala: {i + 1}")
        time.sleep(1)
