from multiprocessing import Process
def worker():
    print("Worker process")
process = Process(target=worker)
process.start()