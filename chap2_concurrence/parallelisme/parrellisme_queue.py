import multiprocessing, time
from multiprocessing import Process, Queue
from multiprocessing.queues import Empty


def make_produit(q):
    for i in range(0, 20):
        q.put(f"Message "+ str(i))
        time.sleep(1)
    q.close()

def consume_produit(q):
    try: 
        while True:
            msg = q.get(timeout=5)
            print(msg) 
    except Empty as empty:
        print("queue is empty close procees")

if __name__ == "__main__":

    q = Queue()
    producteur_process = Process(target=make_produit, args=(q,))
    consommateur_process = Process(target=consume_produit, args=(q,))

    consommateur_process.start()
    producteur_process.start()

    consommateur_process.join()
    producteur_process.join()
