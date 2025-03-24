import time
def retry(func):
    def wrapper():
        for _ in range(3):
            try:
                func()
                break
            except:
                time.sleep(1)
    return wrapper
@retry
def unreliable():
    raise Exception("Error")
unreliable()