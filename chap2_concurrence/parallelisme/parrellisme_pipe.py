import multiprocessing, time
from multiprocessing import Process, Pipe


def make_produit(producteur):
    for i in range(0, 20):
        producteur.send(f"Message "+ str(i))
        time.sleep(1)
    producteur.close()

def consume_produit(consommateur):
    while consommateur.poll(timeout=5):
        message = consommateur.recv()
        print(message)


if __name__ == "__main__":
    producteur, consommateur = Pipe()
    producteur_process = Process(target=make_produit, args=(producteur,))
    consommateur_process = Process(target=consume_produit, args=(consommateur,))

    consommateur_process.start()
    producteur_process.start()

    consommateur_process.join()
    producteur_process.join()
