import threading
def worker():
    print("Worker thread")
thread = threading.Thread(target=worker)
thread.start()