import threading
def worker():
    pass
threads = [threading.Thread(target=worker) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()