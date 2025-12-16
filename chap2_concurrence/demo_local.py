import threading
from threading import local
from random import randint

local_data = local()

def show_value(data):
    try:
        result = data.value
    except AttributeError as e:
        print(threading.current_thread().name + "- no value yet")
    else:
        print(threading.current_thread().name + " "+ str(result))

def worker(data):
    show_value(data)
    data.value = randint(1, 100)
    show_value(data)

local_data.value = "OK"

for i in range(0, 2):
    t = threading.Thread(target=worker, name="T"+str(i), args=(local_data,))
    t.start()
