import time
def slow_function():
    time.sleep(1)
start = time.time()
slow_function()
print("Time taken:", time.time() - start)