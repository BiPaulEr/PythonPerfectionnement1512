from threading import Thread
import os

os.remove("compte.txt")

def ecrire(fichier_path, liste):
    for i in liste:
        with open(fichier_path, "a") as f:
            f.write(str(i)+" "+"\n")
            f.flush()	

threads = []
for i in range(0, 10):
    t = Thread(name=str(i), target=ecrire, args=("compte.txt",range(100, 1000)))
    threads.append(t)
    t.start()
    
list(map(lambda t : t.join(), threads))

for i in range(0, 3):
    t = Thread(name=str(i), target=ecrire, args=("compte.txt",["A", "B", "C", "D","E"]))
    threads.append(t)
    t.start()

