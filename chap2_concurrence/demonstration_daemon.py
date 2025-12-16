from threading import Thread
import threading, time

print(threading.enumerate())

def print_caractere(caractere):
    for i in range(0, 10):
        print(caractere, end="", flush=True)
        time.sleep(1)
    

t1 = Thread(name = "T1", target=print_caractere, args=("*",))
t2 = Thread(name = "T2", daemon=True, target=print_caractere, args=(".",))
t1.start()
t1.join()
t2.start() #**********.
 