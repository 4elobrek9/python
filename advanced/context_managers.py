class MyContextManager:
    def __enter__(self):
        print("Entering context")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
with MyContextManager():
    print("Inside context")