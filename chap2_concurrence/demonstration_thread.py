from threading import Thread
import threading

print(threading.enumerate()) #[<_MainThread(MainThread, started 28956)>]

def simple_worker(name, prenom = "Inconnu"):
    print(f"hello {prenom} {name}")
    print(threading.current_thread())

t = Thread(name = "T1", target=simple_worker, args=("Martin",), kwargs={"prenom": "Pau"})
print(t.ident)
t.start()
print(threading.enumerate()) #[<_MainThread(MainThread, started 28072)>, <Thread(Thread-1 (simple_worker), started 36536)>]
 