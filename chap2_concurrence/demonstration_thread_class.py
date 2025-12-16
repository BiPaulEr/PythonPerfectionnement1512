from threading import Thread
import threading

class Worker(Thread):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        
    def run(self):
        print(f"hello {self.name}")

worker = Worker("MARTIN")
worker.start()