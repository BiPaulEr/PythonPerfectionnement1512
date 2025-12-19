import multiprocessing, time
from multiprocessing import Process


def tache_intensive(name):
    time.sleep(3)
    print(f"Bonjour {name}")


if __name__ == "__main__":
    process1 = Process(target=tache_intensive, args=("PROCESS1",))
    process2 = Process(target=tache_intensive, args=("PROCESS2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
